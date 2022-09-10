
def print_rich_table(title, varibles, data, lines=False):
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
