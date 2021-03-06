# Metlink-Python
Unofficial wrapper for the official metlink API (Requires free api key from metlink)

### Install:
```
pip install metlink-python
```
### Get API KEY
1. Register at [Metlink](https://gwrc-opendata.auth.ap-southeast-2.amazoncognito.com/signup?response_type=token&client_id=4bmn2icphpqls57ijr7k4okv55&redirect_uri=https://opendata.metlink.org.nz/index.html?action=login)
2. Login
3. Get API key from [My Dashboard](https://opendata.metlink.org.nz/dashboard)

### Examples
#### Setup Use
```python
from metlink import metlink

METLINK_API_KEY = 'FakeAPIKEYaiofuhaeaubaaoanaiscai'
metlink = metlink( API_KEY = METLINK_API_KEY )
```
#### Vehicle Positions Example:
```python
from metlink import metlink
metlink = metlink( API_KEY = 'FakeAPIKEYaiofuhaeaubaaoanaiscai' )

vehicle_positions = metlink.get_vehicle_positions()
for position in vehicle_positions:
    print( position.get('bearing'), position.get('latitude'), position.get('longitude') )
```
#### Trip Updates Example:
```python
from metlink import metlink
metlink = metlink( API_KEY = 'FakeAPIKEYaiofuhaeaubaaoanaiscai' )

trip_updates = metlink.get_trip_updates()

for update in trip_updates:
    print( update.get('stop_id'), update.get('arrival_delay'), update.get('arrival_time') )
```
#### Service Alerts Example:
```python
from metlink import metlink
metlink = metlink( API_KEY = 'FakeAPIKEYaiofuhaeaubaaoanaiscai' )

service_alerts = metlink.get_service_alerts()
for index, alert in enumerate(service_alerts):
    print('Alert', index )
    if alert.get('header_text') is not None:
        print( alert.get('header_text') )
    print( 'effect:', alert.get('effect') )
    print( 'cause', alert.get('cause'), '\n' )
```

#### Stop Predictions Example:
```python
from metlink import metlink
metlink = metlink( API_KEY = 'FakeAPIKEYaiofuhaeaubaaoanaiscai' )

stop_predictions = metlink.get_stop_predictions(stop_id=7912)

for pred in stop_predictions:
    if pred.get('status') is not None:
        print(pred.get('service_id'), pred.get('status'))
```

### Functions:
* **get_stop_predictions(stop_id=None)**      
    Passed stop_id, returns list of dictionary's   
    **Param**: stop_id   
    * service_id
    * name
    * vehicle_id
    * direction
    * status
    * trip_id
    * delay
    * monitored
    * operator
    * origin
    * wheelchair_accessible
    * departure
    * arrival

* **get_service_alerts()**   
    Trip Updates - Information about unforeseen events affecting routes, stops, or the network. Given nothing, returns list of dictionaries.   
    **Param**: N/A   
    * active_period
    * effect
    * cause
    * description_text
    * header_text
    * severity_level
    * informed_entity

* **get_vehicle_positions()**   
    Vehicle Positions - API to get Information about vehicles including location. Given nothing, returns list of dictionaries. if no busses are active returns empty list   
    **Param**: N/A   
    * vehicle_id
    * bearing
    * latitude
    * longitude

* **get_trip_updates()**   
    Trip Updates - Delays, cancellations, changed routes. Given nothing, returns list of dictionaries. returns empty list if no trip delays or changes   
    **Param**: N/A   
    * stop_id
    * arrival_delay
    * arrival_time
    * trip_start_time
    * vehicle_id

* **get_routes(stop_id=None)**   
    Returns list of dictionarys of route infomation, optionally given stop_id as filter   
    **Param**: Optional stop_id   
    * id
    * route_id
    * agency_id
    * route_short_name
    * route_long_name
    * route_desc
    * route_type
    * route_color
    * route_text_color
    * route_url

* **get_stops(trip_id=None, route_id=None)**   
    Returns list of dictionarys of stops infomation, optionally given trip_id and or route_id   
    **Param**: Optional stop_id
    * id
    * stop_id
    * stop_code
    * stop_name
    * stop_desc
    * zone_id
    * stop_lat
    * stop_lon
    * location_type
    * parent_station
    * stop_url
    * stop_timezone
