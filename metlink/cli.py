import argparse
from metlink import Metlink
from metlink.constants import CLI_ARGUMENTS, CLI_HELP, CLI_PRINT_ARGUMENTS


class CLI(argparse.ArgumentParser):
    '''
    Metlink CLI
    --------------------
    CLI for Metlink API using argparse module.

    Python File:
    --------------------
    Create file to call with options, eg 'metlink.py' and add the following:
    ```python
        from metlink import CLI

        CLI('api_key)
    ```

    Usage:
    --------------------
        python {python file} [options]

    Options:
    --------------------
        -h, --help                  Show this help message and exit

        -v, --version               Show program's version number

        --stops                     Prints stop information, optional
        filters: --trip, --route

        --routes                    Prints route information, optional
        filter: --stop

        --vehicle_positions         Prints vehicle positions

        --trip_updates              Prints trip updates

        --service_alerts            Prints service alerts

        --stop_predictions          Prints stop predictions, optional
        filter: --stop

        --rich                      Use rich module to style table

        --stop <stop>               Select Stop

        --route <route>             Select Route

        --trip <trip>               Select Trip


    Example:
    --------------------
        python metlink.py --help

        python metlink.py --trip_updates

        python metlink.py --trip_updates --rich

        python metlink.py --stop 5000 --routes --rich
    '''
    def __init__(self, api_key: str, *args, **kwargs):
        super().__init__(add_help=False, *args, **kwargs)
        self.metlink = Metlink(api_key)
        self.__add_args()
        self.__parse_args()

    def __parse_args(self, *args, **kwargs):
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
        for title_info in CLI_PRINT_ARGUMENTS:
            if getattr(args, title_info['name']):
                title = title_info['name'].title().replace('_', ' ')
                columns = title_info['columns']
                method_name = f'get_{title_info["name"]}'
                method_args = {
                    'stop_id': args.stop,
                    'trip_id': args.trip,
                    'route_id': args.route
                }
                print_table(
                    title,
                    columns,
                    getattr(self.metlink, method_name)(**method_args)
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
