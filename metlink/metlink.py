import urllib3
import json
import certifi
from metlink import constants as const


class Metlink():
    '''
        Class contains methods to access the Metlink API.

        Methods:
                get_stops(trip: str = None, route: str = None)
                get_routes(stop_id: str = None)
                get_vehicle_positions()
                get_trip_updates()
                get_service_alerts()
                get_stop_predictions(stop_id: str)

        Parameters:
                API_KEY (str): API key to access Metlink API
    '''
    __version__ = '0.0.7'

    def __init__(self, API_KEY=None):
        self.API_KEY = API_KEY
        self.http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where()
        )
        if self.API_KEY is None:
            raise ValueError('API_KEY parameter not provided to Metlink class')

    def __get_metlink_data(self, API_Path: str):
        '''
            Get JSON object of data from given path,
            if response status is not 200 throws Value Error

            Parameters:
                    API_Path (string): URL of path to call

            Returns:
                    (JSON Object): JSON object contains
                    data in the form of key/value pair.
        '''
        try:
            r = self.http.request(
                'GET',
                API_Path,
                headers={
                    'accept': 'application/json',
                    'x-api-key': self.API_KEY
                }
            )
            if r.status != 200:
                raise ValueError('Response status not 200')
        except urllib3.exceptions.MaxRetryError:
            raise ValueError('Maximum retries exceeded, check internet.')
        except urllib3.exceptions.NewConnectionError:
            raise ValueError('Connection failed, check internet.')
        except urllib3.exceptions.SSLError:
            raise ValueError('SSL Error, check internet.')
        except urllib3.exceptions.HTTPError:
            raise ValueError('HTTP Error, check internet.')
        except urllib3.exceptions.ConnectionError:
            raise ValueError('Connection Error, check internet.')

        return json.loads(r.data.decode('utf-8'))

    def get_stops(self, trip: str = None, route: str = None):
        '''
            Gets stop information for all or a specific trip or route.

            Parameters:
                    trip (str): Optionally provide trip id
                    route (str): Optionally provide route id

            Returns:
                    (list[dict[str, str]]): Returns list of dictionaries each
                    dictionary contains information about a stop.
        '''
        url = const.STOPS_URL
        if trip and route:
            url += '?trip_id=' + trip + '&route_id=' + route
        elif trip:
            url += '?trip_id=' + trip
        elif route:
            url += '?route_id=' + route
        routes = []
        for entity in self.__get_metlink_data(url):
            curr_route = {
                'id': entity['id'],
                'stop_id': entity['stop_id'],
                'stop_code': entity['stop_code'],
                'stop_name': entity['stop_name'],
                'stop_desc': entity['stop_desc'],
                'zone_id': entity['zone_id'],
                'stop_lat': entity['stop_lat'],
                'stop_lon': entity['stop_lon'],
                'location_type': entity['location_type'],
                'parent_station': entity['parent_station'],
                'stop_url': entity['stop_url'],
                'stop_timezone': entity['stop_timezone'],
            }
            routes.append(curr_route)
        return routes

    def get_routes(self, stop_id: str = None):
        '''
            Gets route information for all or a specific stop.

            Parameters:
                    stop_id (str): Optionally provide stop id

            Returns:
                    (list[dict[str, str]]): Returns list of
                    dictionaries each dictionary
                    contains information about a route.
        '''
        url = const.ROUTES_URL
        if stop_id:
            url += '?stop_id=' + str(stop_id)
        routes = []
        for entity in self.__get_metlink_data(url):
            route = {
                'id': entity['id'],
                'route_id': entity['route_id'],
                'agency_id': entity['agency_id'],
                'route_short_name': entity['route_short_name'],
                'route_long_name': entity['route_long_name'],
                'route_desc': entity['route_desc'],
                'route_type': entity['route_type'],
                'route_color': entity['route_color'],
                'route_text_color': entity['route_text_color'],
                'route_url': entity['route_url'],
            }
            routes.append(route)
        return routes

    def get_vehicle_positions(self):
        '''
            Gets active bus locations.

            Returns:
                    (list[dict[str, str]]): Returns list of dictionaries
                    each dictionary contains information about a bus
                    and its position.
        '''
        response = self.__get_metlink_data(const.VEHICLE_POSITIONS_URL)
        vehicle_positions = []
        for entity in response['entity']:
            vehicle_position = {
                'vehicle_id': entity['vehicle']['vehicle']['id'],
                'bearing': entity['vehicle']['position']['bearing'],
                'latitude': entity['vehicle']['position']['latitude'],
                'longitude': entity['vehicle']['position']['longitude']
            }
            vehicle_positions.append(vehicle_position)
        return vehicle_positions

    def get_trip_updates(self):
        '''
            Gets Delays, cancellations, changed routes.

            Returns:
                    (list[dict[str, str]]): Returns list of dictionaries
                    each dictionary contains stop id, vehicle id and
                    new trip times.
        '''
        response = self.__get_metlink_data(const.TRIP_UPDATES_URL)
        trip_updates = []
        for entity in response['entity']:
            trip = entity['trip_update']
            trip_update = {
                'stop_id': trip['stop_time_update']['stop_id'],
                'arrival_delay': trip['stop_time_update']['arrival']['delay'],
                'arrival_time': trip['stop_time_update']['arrival']['time'],
                'trip_start_time': trip['trip']['start_time'],
                'vehicle_id': trip['vehicle']['id'],
            }
            trip_updates.append(trip_update)
        return trip_updates

    def get_service_alerts(self):
        '''
            Information about unforeseen
            events affecting routes, stops, or the network.

            Returns:
                    (list[dict[str, str]]): Returns list of dictionaries
                    each dictionary contains warning information.
        '''
        response = self.__get_metlink_data(const.SERVICE_ALERTS_URL)
        service_alerts = []
        for entity in response['entity']:
            des = entity['alert']['description_text']['translation'][0]['text']
            head = entity['alert']['header_text']['translation'][0]['text']
            service_alert = {
                'active_period': entity['alert']['active_period'],
                'effect': entity['alert']['effect'],
                'cause': entity['alert']['cause'],
                'description_text': des,
                'header_text': head,
                'severity_level': entity['alert']['severity_level'],
                'informed_entity': entity['alert']['informed_entity'],
                # 'id': entity['alert']['id'],
                # 'timestamp': entity['alert']['timestamp']
            }
            service_alerts.append(service_alert)
        return service_alerts

    def get_stop_predictions(self, stop_id: str = None):
        '''
            Get all stop predictions for given stop.

            Parameters:
                    stop_id (str): Stop id

            Returns:
                    (list[dict[str, str]]): Returns list of dictionaries
                    each dictionary contains a stop prediction for the
                    given stop.
        '''
        if stop_id:
            response = self.__get_metlink_data(
                 const.STOP_PREDICTIONS_URL + '?stop_id=' + str(stop_id))
            stop_predictions = []
            for stop in response['departures']:
                prediction = {
                    'service_id': stop['service_id'],
                    'name': stop['name'],
                    'vehicle_id': stop['vehicle_id'],
                    'direction': stop['direction'],
                    'status': stop['status'],
                    'trip_id': stop['trip_id'],
                    'delay': stop['delay'],
                    'monitored': stop['monitored'],
                    'operator': stop['operator'],
                    'origin': stop['origin'],
                    'wheelchair_accessible': stop['wheelchair_accessible'],
                    'departure': stop['departure'],
                    'arrival': stop['arrival']
                }
                stop_predictions.append(prediction)
            return stop_predictions

        raise ValueError('stop_id must be given for get_stop_predictions')
