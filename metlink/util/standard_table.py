
def print_standard_table(title, varibles, data, lines=False):
    print(title)
    for var in varibles:
        print(var + ', ', end='')
    print()
    for row in data:
        for var in varibles:
            print(
                row.get(var.replace(' ', '_').lower()) + ', ', end='')
        print()
