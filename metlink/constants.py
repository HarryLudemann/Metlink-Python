# Metlink API URL's
BASE_URL = 'https://api.opendata.metlink.org.nz/v1/'
STOPS_URL = BASE_URL + 'gtfs/stops'
ROUTES_URL = BASE_URL + 'gtfs/routes'
VEHICLE_POSITIONS_URL = BASE_URL + 'gtfs-rt/vehiclepositions'
TRIP_UPDATES_URL = BASE_URL + 'gtfs-rt/tripupdates'
SERVICE_ALERTS_URL = BASE_URL + 'gtfs-rt/servicealerts'
STOP_PREDICTIONS_URL = BASE_URL + 'stop-predictions'

# all the CLI arguments, except help and version information for argparse
CLI_ARGUMENTS = [
    # Style Table
    {
        'name': '--rich',
        'action': 'store_true',
        'help': 'Use rich module to style table',
    },
    # API Filters
    {
        'name': '--stop',
        'action': 'store',
        'type': str,
        'help': 'Select Stop',
    }, {
        'name': '--route',
        'action': 'store',
        'type': str,
        'help': 'Select Route',
    }, {
        'name': '--trip',
        'action': 'store',
        'type': str,
        'help': 'Select Trip',
    },
    # API Information to display
    {
        'name': '--stops',
        'action': 'store_true',
        'help': 'Prints stop information, optional filters: --trip, --route',
    }, {
        'name': '--routes',
        'action': 'store_true',
        'help': 'Prints route information, optional filter: --stop',
    }, {
        'name': '--vehicle_positions',
        'action': 'store_true',
        'help': 'Prints vehicle positions',
    }, {
        'name': '--trip_updates',
        'action': 'store_true',
        'help': 'Prints trip updates',
    }, {
        'name': '--service_alerts',
        'action': 'store_true',
        'help': 'Prints service alerts',
    }, {
        'name': '--stop_predictions',
        'action': 'store_true',
        'help': 'Prints stop predictions, optional filter: --stop',
    },
]

# arguments to print for each 'API Information to display' above
# eg for first item stops, prints Stop Name or stop_name etc
CLI_PRINT_ARGUMENTS = [
    {
        'name': 'stops',
        'columns': ['Stop Name', 'Stop Description', 'Stop ID']
    },
    {
        'name': 'routes',
        'columns': ['Route Short Name', 'Route Long Name']
    },
    {
        'name': 'vehicle_positions',
        'columns': ['Bearing', 'Latitude', 'Longitude']
    },
    {
        'name': 'trip_updates',
        'columns': ['Stop ID', 'Arrival Delay', 'Arrival Time']
    },
    {
        'name': 'service_alerts',
        'columns': ['Header Text', 'Effect', 'Cause',
                    'Severity Level']
    },
    {
        'name': 'stop_predictions',
        'columns': ['Service ID', 'Status', 'Trip ID']
    }
]


CLI_HELP = """
Arguments:
    -h, --help                show this help message
    -v, --version             show program's version number

    Style Table:
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
"""
