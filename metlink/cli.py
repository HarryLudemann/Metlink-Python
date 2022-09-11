from metlink import Metlink
import argparse
from metlink.util.interface.standard_table import print_standard_table
from metlink.util.interface.rich_table import print_rich_table
from metlink.util.data_controller import DataController


def help() -> str:
    return """
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
        --data-types                Show static names and vars
        --data NAME                 Prints static data, given name

"""


class CLI:
    '''
        Class when instansiated will parse arguments and display information
        from the metlink api, call -h or --help to see all arguments.

        Parameters:
            api_key (str): Metlink api key
    '''
    lines = False
    rich_style = False
    data_controller = DataController()

    def __init__(self, api_key: str):
        metlink = Metlink(api_key)
        parser = self.create_parser(metlink.__version__)
        args = parser.parse_args()  # get args
        self.lines = True if args.lines else False
        self.rich_style = True if args.rich else False
        self.handle_args(args, metlink)

    def create_parser(self, version):
        parser = argparse.ArgumentParser(add_help=False,)
        parser.add_argument(
            '-v', '--version',
            action='version',
            version=version
        )
        # show lines between rows and columns
        parser.add_argument(
            '--lines',
            action='store_true',
            help='Show lines between rows',
        )
        parser.add_argument(
            '--rich',
            action='store_true',
            help='Use Rich module to style table',
        )
        # filter inputs
        parser.add_argument("--stop", type=str, help="Select Stop")
        parser.add_argument("--route", type=str, help="Select Route")
        parser.add_argument("--trip", type=str, help="Select Trip")
        parser.add_argument(
            "--filter_name", type=str, help="Select Filter Name")
        parser.add_argument(
            "--filter_value", type=str, help="Select Value Name")
        parser.add_argument(
            "--data", type=str, help="Print possible static data")
        # information to display
        parser.add_argument(
            '--stops',
            action='store_true',
            help='Prints stop information, optional filters: --trip, --route'
        )
        parser.add_argument(
            '--routes',
            action='store_true',
            help='Prints route information, optional filter: --stop'
        )
        parser.add_argument(
            '--vehicle_positions',
            action='store_true',
            help='Prints vehicle positions'
        )
        parser.add_argument(
            '--trip_updates',
            action='store_true',
            help='Prints trip updates'
        )
        parser.add_argument(
            '--service_alerts',
            action='store_true',
            help='Prints service alerts'
        )
        parser.add_argument(
            '--stop_predictions',
            action='store_true',
            help='Prints stop predictions, optional filter: --stop'
        )
        parser.add_argument(
            '-h', '--help',
            action='store_true',
            help='Show this help message and exit'
        )
        parser.add_argument(
            '--data_types',
            action='store_true',
            help='Show possible static data, eg. routes, stops'
        )
        return parser

    def handle_args(self, args, metlink: Metlink):
        if args.stops:
            self.print_table(
                'Stops Information',
                ['Stop Name', 'Stop Description', 'Stop ID'],
                metlink.get_stops(trip=args.trip, route=args.route)
            )

        if args.routes:
            self.print_table(
                'Routes Information',
                ['Route Short Name', 'Route Long Name'],
                metlink.get_routes(stop_id=args.stop)
            )

        if args.vehicle_positions:
            self.print_table(
                'Vehicle Positions',
                ['Bearing', 'Latitude', 'Longitude'],
                metlink.get_vehicle_positions()
            )

        if args.trip_updates:
            self.print_table(
                'Trip Updates',
                ['Stop ID', 'Arrival Delay', 'Arrival Time'],
                metlink.get_trip_updates()
            )

        if args.service_alerts:
            self.print_table(
                'Service Alerts',
                ['Header Text', 'Effect', 'Cause', 'Severity Level'],
                metlink.get_service_alerts()
            )

        if args.stop_predictions:
            self.print_table(
                'Stop Predictions',
                ['Service ID', 'Status', 'Trip ID'],
                metlink.get_stop_predictions(stop_id=args.stop)
            )

        if args.data_types:
            self.data_controller.print_possible_data()

        if args.data:
            if args.filter_name and args.filter_value:
                self.data_controller.print_data(
                    name=args.data,
                    filters={args.filter_name: args.filter_value},
                    rich=args.rich)
            else:
                self.data_controller.print_data(args.data, False)

        if args.help:
            print(help())

    def print_table(self, title, varibles, data):
        '''
            Print table, either with raw python or using rich module
            Past Varible names can have capital letters and spacing,
            although the data must have no capital letters only underscores

            Parameters:
                title (str): Title of table
                varibles (list): List of varible names to display
                data (list): List of dictionaries to display
        '''
        if self.rich_style:
            print_rich_table(title, varibles, data, self.lines)
        else:
            print_standard_table(title, varibles, data, self.lines)
