from metlink import Metlink
import os


def get_api_key():
    """ Gets the API key from the .env file """
    if os.getenv('METLINK_API_KEY'):
        print("Using github secret API key")
        return os.environ['METLINK_API_KEY']
    else:
        print('Using local API key')
        from dotenv import load_dotenv
        load_dotenv()
        return os.environ['METLINK_API_KEY']


def test_creation():
    """ Tests the main class object is instantiable """
    metlink_obj = Metlink(get_api_key())
    assert metlink_obj is not None


def test_get_stops():
    """ Tests the get_stops method """
    metlink_obj = Metlink(get_api_key())
    stops = metlink_obj.get_stops()
    assert stops is not None


def test_get_routes():
    """ Tests the get_routes method """
    metlink_obj = Metlink(get_api_key())
    routes = metlink_obj.get_routes()
    assert routes is not None


def test_vehicle_positions():
    """ Tests the get_vehicle_positions method """
    metlink_obj = Metlink(get_api_key())
    vehicle_positions = metlink_obj.get_vehicle_positions()
    assert vehicle_positions is not None


def test_trip_updates():
    """ Tests the get_trip_updates method """
    metlink_obj = Metlink(get_api_key())
    trip_updates = metlink_obj.get_trip_updates()
    assert trip_updates is not None


def test_service_alerts():
    """ Tests the get_service_alerts method """
    metlink_obj = Metlink(get_api_key())
    service_alerts = metlink_obj.get_service_alerts()
    assert service_alerts is not None


def test_stop_predictions():
    """ Tests the get_stop_predictions method """
    metlink_obj = Metlink(get_api_key())
    stop_predictions = metlink_obj.get_stop_predictions(stop_id=5000)
    assert stop_predictions is not None
