import json


def get_data(data_list):
    try:
        with open(data_list) as file:
            return json.load(file)
    except(IOError, ValueError, FileNotFoundError, json.JSONDecodeError):
        return []


def set_data(data, data_list):
    try:
        with open(data_list, 'w') as f_write:
            return json.dump(data, f_write)
    except ValueError:
        return data_list
