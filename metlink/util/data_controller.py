import csv
from metlink.util.interface.standard_table import print_standard_table
from metlink.util.interface.rich_table import print_rich_table


class DataController:
    class Data:
        def __init__(self, name, variables, data):
            self.data = data
            self.variables = variables
            self.name = name

    data = {}

    def load_data(self, path):
        try:
            with open(path, 'r') as f:
                csv_file = csv.reader(f)
                variables = next(csv_file)
                data = [dict(zip(variables, row)) for row in csv_file]
                name = path.split('/')[-1].split('.')[0]
                self.data[name] = self.Data(name, variables, data)
                return True
        except FileNotFoundError:
            print('File not found: ' + path)
            return False

    def print_data(self, name: str, rich, filters=None):
        """
        Prints the data in a nice table

        Args:
            name: str - The name of the data to print
            filters: dict - A dictionary of filters to apply to the data
        """
        if name in self.data:
            if filters is not None:
                data = self.data[name].data
                for key, value in filters.items():
                    data = [row for row in data if row[key] == value]
            else:
                data = self.data[name].data
            if len(data) > 0:
                if rich:
                    print_rich_table(
                        self.data[name].name,
                        self.data[name].variables,
                        data,
                        lines=False)
                else:
                    print_standard_table(
                        self.data[name].name,
                        self.data[name].variables,
                        data,
                        lines=False)
        else:
            if self.load_data('data/' + name + '.csv'):
                self.print_data(name, filters)

    def print_possible_data(self):
        import os
        for file in os.listdir('data/'):
            if file.endswith('.csv'):
                with open('data/' + file, 'r') as f:
                    csv_file = csv.reader(f)
                    variables = next(csv_file)
                    print(file.split('.')[0] + ': ' + ', '.join(variables))
