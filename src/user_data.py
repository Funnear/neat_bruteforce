import json


def user_data():
    _file = 'resources/user_data.json'
    with open(_file) as user_data_file:
        _user = json.load(user_data_file)
        return _user
