import requests


class metlink():
    __version__ = '0.1'
    base_url = 'https://api.opendata.metlink.org.nz/v1/'

    def __init__(self, API_KEY = None):
        self.API_KEY = API_KEY



    # GTFS-RT APIS - Real time data from the public transport network.

    def get_rt_data(self, API_name):
        """ Method passed API Name eg 'vehiclepositions' and returns response"""
        headers = {
        'accept': 'application/json',
        'x-api-key': self.API_KEY
        }
        response = requests.get(self.base_url + 'gtfs-rt/' + API_name, headers=headers)
        return response

    def get_vehicle_positions(self):
        """ Vehicle Positions -  API to get Information about vehicles including location.
            Given nothing, returns list of dictionaries.
        """
        response = self.get_rt_data('vehiclepositions') 
        vehicle_positions = []
        for entity in response.json()['entity']:
            vehicle_position = {
                'vehicle_id': entity['vehicle']['vehicle']['id'],
                'bearing': entity['vehicle']['position']['bearing'],
                'latitude': entity['vehicle']['position']['latitude'],
                'longitude': entity['vehicle']['position']['longitude']
            }
            vehicle_positions.append(vehicle_position)
        return vehicle_positions


    def get_trip_updates(self):
        """ Trip Updates - Delays, cancellations, changed routes.
            Given nothing, returns list of dictionaries.
        """
        response = self.get_rt_data('tripupdates')
        trip_updates = []
        for entity in response.json()['entity']:
            trip_update = {
                'stop_id': entity['trip_update']['stop_time_update']['stop_id'],
                'arrival_delay': entity['trip_update']['stop_time_update']['arrival']['delay'],
                'arrival_time': entity['trip_update']['stop_time_update']['arrival']['time'],
                'trip_start_time': entity['trip_update']['trip']['start_time'],
                'vehicle_id': entity['trip_update']['vehicle']['id'],
            }
            trip_updates.append(trip_update)
        return trip_updates


    def get_service_alerts(self):
        """ Trip Updates - Information about unforeseen events affecting routes, stops, or the network.
            Given nothing, returns list of dictionaries.
        """
        response = self.get_rt_data('servicealerts') 
        service_alerts = []
        for entity in response.json()['entity']:
            service_alert = {
                'active_period': entity['alert']['active_period'],
                'effect': entity['alert']['effect'],
                'cause': entity['alert']['cause'],
                'description_text': entity['alert']['description_text']['translation'][0]['text'],
                'header_text': entity['alert']['header_text']['translation'][0]['text'],
                'severity_level': entity['alert']['severity_level'],
                'informed_entity': entity['alert']['informed_entity'],
                #'id': entity['alert']['id'],
                #'timestamp': entity['alert']['timestamp']
            }
            service_alerts.append(service_alert)
        return service_alerts

            


    # stop predicion API

    def get_stop_predictions(self, stop_id):
        """ Passed stop_id, returns list of dictionary's """
        headers = {
        'accept': 'application/json',
        'x-api-key': self.API_KEY
        }
        response = requests.get(self.base_url + 'stop-predictions?stop_id=' + str(stop_id), headers=headers)

        stop_predictions = []
        for stop in response.json()['departures']:
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