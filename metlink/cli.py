import argparse
from metlink import Metlink
from metlink.constants import CLI_ARGUMENTS, CLI_HELP


class CLI(argparse.ArgumentParser, Metlink):
    def __init__(self, api_key: str, *args, **kwargs):
        super().__init__(add_help=False, *args, **kwargs)
        self.metlink = Metlink(api_key)
        self.__add_args()
        self.parse_args()

    def parse_args(self, *args, **kwargs):
        args = super().parse_args(*args, **kwargs)
        if args.help:
            print(CLI_HELP)
        else:
            self.__handle_args(args)

    def __add_args(self):
        self.add_argument('-v', '--version', action='version',
                          version=self.metlink.__version__)
        self.add_argument('-h', '--help', action='store_true',
                          help='Show this help message and exit')
        for arg in CLI_ARGUMENTS:
            self.add_argument(arg.pop('name'), **arg)

    def __handle_args(self, args):
        print_table = standard_table if not args.rich else rich_table
        if args.stops:
            print_table(
                'Stops Information',
                ['Stop Name', 'Stop Description', 'Stop ID'],
                self.metlink.get_stops(trip=args.trip, route=args.route)
            )

        if args.routes:
            print_table(
                'Routes Information',
                ['Route Short Name', 'Route Long Name'],
                self.metlink.get_routes(stop_id=args.stop)
            )

        if args.vehicle_positions:
            print_table(
                'Vehicle Positions',
                ['Bearing', 'Latitude', 'Longitude'],
                self.metlink.get_vehicle_positions()
            )

        if args.trip_updates:
            print_table(
                'Trip Updates',
                ['Stop ID', 'Arrival Delay', 'Arrival Time'],
                self.metlink.get_trip_updates()
            )

        if args.service_alerts:
            print_table(
                'Service Alerts',
                ['Header Text', 'Effect', 'Cause', 'Severity Level'],
                self.metlink.get_service_alerts()
            )

        if args.stop_predictions:
            print_table(
                'Stop Predictions',
                ['Service ID', 'Status', 'Trip ID'],
                self.metlink.get_stop_predictions(stop_id=args.stop)
            )


def standard_table(title, variables, data):
    """
    Prints a table with the given title, variables and data.

    Args:
        title (str): The title of the table.
        variables (list): list of the variables to be printed.
        data (list): list of dictionaries containing the data.
    """
    print(title)
    # add column names
    for column in variables:
        print(column + ', ', end='')
    print()
    # add rows/data
    for row in data:
        for var in variables:
            print(
                row.get(var.replace(' ', '_').lower()) + ', ', end='')
        print()


def rich_table(title, variables, data):
    """
    Prints a table with the given title, variables and data.
    Using the rich library.

    Args:
        title (str): The title of the table.
        variables (list): list of the variables to be printed.
        data (list): list of dictionaries containing the data.

    """
    from rich.table import Table
    from rich.console import Console
    console = Console()
    table = Table(
            title=title,
            header_style="bold white",
            border_style="magenta",
            row_styles=["white", "dim white"],
            show_lines=False,
            show_header=True,
            show_footer=False,
        )
    variables_ids = []
    # add column names, and get the ids of the variables
    for var in variables:
        table.add_column(var)
        variables_ids.append(var.replace(' ', '_').lower())
    # add rows/data
    for row in data:
        table.add_row(*[row.get(var) for var in variables_ids])
    console.print(table)
