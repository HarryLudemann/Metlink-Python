
def print_standard_table(title, varibles, data, lines=False):
    """
    Prints a table with the given title, varibles and data.

    Args:
        title (str): The title of the table.
        varibles (list): A list of the varibles to be printed.
        data (list): A list of dictionaries containing the data.
        lines (bool, optional): Whether to print lines between
        rows. Defaults to False.
    """
    print(title)
    for var in varibles:
        print(var + ', ', end='')
    print()
    for row in data:
        for var in varibles:
            print(
                row.get(var.replace(' ', '_').lower()) + ', ', end='')
        print()
