
def print_rich_table(title, varibles, data, lines=False):
    """
    Prints a table with the given title, varibles and data.
    Using the rich library.

    Args:
        title (str): The title of the table.
        varibles (list): A list of the varibles to be printed.
        data (list): A list of dictionaries containing the data.
        lines (bool, optional): Whether to print lines between
        rows. Defaults to False.

    """
    from rich.table import Table
    from rich.console import Console
    console = Console()
    table = Table(
            title=title,
            header_style="bold white",
            border_style="magenta",
            row_styles=["white", "dim white"],
            show_lines=lines,
            show_header=True,
            show_footer=False,
        )
    varibles_ids = []
    for var in varibles:
        table.add_column(var)
        varibles_ids.append(var.replace(' ', '_').lower())
    for row in data:
        table.add_row(*[row.get(var) for var in varibles_ids])
    console.print(table)
