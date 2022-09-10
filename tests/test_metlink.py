from metlink import Metlink
import os

# check if METLINK_API_KEY env variable is set
# if 'METLINK_API_KEY' in os.environ['METLINK_API_KEY']:
API_KEY = os.environ['METLINK_API_KEY']
# else:
#     from dotenv import load_dotenv
#     load_dotenv()
#     API_KEY = os.environ['METLINK_API_KEY']


def test_creation():
    """ Tests the main class object is instantiable """
    metlink_obj = Metlink(API_KEY)
    assert metlink_obj is not None


def test_get_stops():
    """ Tests the get_stops method """
    metlink_obj = Metlink(API_KEY)
    stops = metlink_obj.get_stops()
    assert stops is not None


def test_get_routes():
    """ Tests the get_routes method """
    metlink_obj = Metlink(API_KEY)
    routes = metlink_obj.get_routes()
    assert routes is not None


def test_vehicle_positions():
    """ Tests the get_vehicle_positions method """
    metlink_obj = Metlink(API_KEY)
    vehicle_positions = metlink_obj.get_vehicle_positions()
    assert vehicle_positions is not None


def test_trip_updates():
    """ Tests the get_trip_updates method """
    metlink_obj = Metlink(API_KEY)
    trip_updates = metlink_obj.get_trip_updates()
    assert trip_updates is not None


def test_service_alerts():
    """ Tests the get_service_alerts method """
    metlink_obj = Metlink(API_KEY)
    service_alerts = metlink_obj.get_service_alerts()
    assert service_alerts is not None
