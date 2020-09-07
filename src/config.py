import configparser


def get(key):
    config = configparser.ConfigParser()
    config.read('./resources/client.config')
    auth_url = config['DEFAULT'][key]
    return auth_url
