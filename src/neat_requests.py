import requests
from src.precept import Precept
from src import config


def response_analyst(status_code):
    if status_code == 200:
        print('Authentication passed.')
        return Precept.SUCCESS
    elif status_code == 401:
        return Precept.CONTINUE
    elif status_code == 500:
        print('Server Down')
        return Precept.STOP
    elif status_code == 429:
        print('Too many requests')
        return Precept.STOP
    else:
        print('Suspicious server behavior.')
        return Precept.STOP


def auth_request(login, password):
    auth_url = config.get('auth_url')
    try:
        _response = requests.post(auth_url,
                                  json={'login': login, 'password': password})
        return response_analyst(_response.status_code)
    except requests.exceptions.ConnectionError as e1:
        print(f'\nConnection error happened for url:\n{auth_url}\n')
        print(f'Context:\n{e1.__context__}')
        return Precept.STOP
    except requests.exceptions.HTTPError as e2:
        print('\nHTTP Error occurred for request:\n')
        print({e2})
        return Precept.STOP
