# Metlink-Python
[![](https://github.com/HarryLudemann/Metlink-Python/workflows/pytests/badge.svg)]()
[![Maintainability](https://api.codeclimate.com/v1/badges/08e4dc1f109aaa6c4f75/maintainability)](https://codeclimate.com/github/HarryLudemann/Metlink-Python/maintainability)
   
Python wrapper and CLI for the [Wellington Metlink's](https://gwrc-opendata.auth.ap-southeast-2.amazoncognito.com/signup?response_type=token&client_id=4bmn2icphpqls57ijr7k4okv55&redirect_uri=https://opendata.metlink.org.nz/index.html?action=login) API and static data, this requires a free api key from [Metlink](https://gwrc-opendata.auth.ap-southeast-2.amazoncognito.com/signup?response_type=token&client_id=4bmn2icphpqls57ijr7k4okv55&redirect_uri=https://opendata.metlink.org.nz/index.html?action=login).

### Install Module:
```
pip install metlink-python
```
or
```
pip3 install metlink-python
```
### Get API KEY
1. Register at [Metlink](https://gwrc-opendata.auth.ap-southeast-2.amazoncognito.com/signup?response_type=token&client_id=4bmn2icphpqls57ijr7k4okv55&redirect_uri=https://opendata.metlink.org.nz/index.html?action=login)
2. Login
3. Get API key from [My Dashboard](https://opendata.metlink.org.nz/dashboard)

### CLI
#### Setup:
Create python file containing the following code with your API key, for example called 'main.py' containing:
```python
from metlink import CLI

CLI('FakeAPIKEYaiofuhaeaubaaoanaiscai')
```
#### Test:
Then run the created script with the argument '-h' to display all arguments.
```
python main.py -h
```
or 
```
python3 main.py -h
```
Returning:
```
Arguments:
    -h, --help                show this help message
    -v, --version             show program's version number

    Style Table:
        --lines               Show lines between rows
        --rich                Use rich module to style table

    API Filters:
        --stop STOP      Select Stop
        --route ROUTE   Select Route
        --trip TRIP      Select Trip

    API Information to display:
        --stops                   Prints stop information,
                                    filters: --trip, --route
        --routes                  Prints route information,
                                    filters: --stop
        --vehicle_positions       Prints vehicle positions,
                                    filters: N/A
        --trip_updates            Prints trip updates,
                                    filters: N/A
        --service_alerts          Prints service alerts,
                                    filters: N/A
        --stop_predictions        Prints stop predictions,
                                    filters: --stop

    Static Data Filters:
        --filter_name FILTER_NAME       Select Filter Name
        --filter_value FILTER_VALUE     Select Value Name
    
    Static Data Information to display:
        --data-types                Show possible static data and their variables
        --data NAME                 Prints static data, given name
```
#### Optionally Install Rich Module
Optionally you can install the rich module to visually make the returned tables more attractive.
```python
pip install rich
```
or
```python
pip3 install rich
```
#### API Example:
For example run this command to get a table of service alerts, note this example requires the rich module (remove --rich to use without).
```
python main.py --service_alerts --rich
```
or 
```
python3 main.py --service_alerts --rich
```
#### Static Example
Note this example requires the rich module (remove --rich to use without).
```python
python main.py --data routes --filter_name route_id --filter_value 10 --rich
```
or 
```python
python main.py --data routes --filter_name route_id --filter_value 10 --rich
```
### Python Module
#### Initialize Module:
To use any of the functions you need to initialize the class at the start of the script.
```python
from metlink import Metlink

metlink = Metlink('FakeAPIKEYaiofuhaeaubaaoanaiscai')
```
#### Vehicle Positions Example:
```python
vehicle_positions = metlink.get_vehicle_positions()
for position in vehicle_positions:
    print( position.get('bearing'), position.get('latitude'), position.get('longitude') )
```
#### Trip Updates Example:
```python
trip_updates = metlink.get_trip_updates()

for update in trip_updates:
    print( update.get('stop_id'), update.get('arrival_delay'), update.get('arrival_time') )
```
#### Service Alerts Example:
```python
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
stop_predictions = metlink.get_stop_predictions(stop_id=7912)

for pred in stop_predictions:
    if pred.get('status') is not None:
        print(pred.get('service_id'), pred.get('status'))
```

#### Module Functions:
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
    **Param**: Optional trip_id and or route_id
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


