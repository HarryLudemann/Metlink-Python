import os


def txt_to_csv():
    """Converts all txt files in data to csv files"""
    for file in os.listdir('data'):
        if file.endswith('.txt'):
            os.rename(f'data/{file}', f'data/{file[:-4]}.csv')


def test_csv():
    """ Test there are no .txt files in data folder"""
    for file in os.listdir('data'):
        if file.endswith('.txt'):
            print("There are .txt files in data folder, testing conversion")
            try:
                txt_to_csv()
                print("Conversion successful")
                assert test_csv()
            except AssertionError:
                print("There are still .txt files in data folder")
                break
            assert False
    assert True


def test_routes_load():
    """Test that routes load"""
    from metlink.util.data_controller import DataController
    data_controller = DataController()
    assert data_controller.load_data('data/routes.csv')
