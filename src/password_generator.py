import string

from src import config


def password_generator():
    alphabet = string.digits
    alphabet += string.ascii_lowercase
    base = len(alphabet)

    shift = 0
    length = int(config.get('minimal_password_length'))

    while True:
        password = ''
        temp = shift
        while temp > 0:
            k = temp // base
            rest = temp % base
            password = alphabet[rest] + password
            temp = k

        while len(password) < length:
            password = alphabet[0] + password

        yield password

        if alphabet[-1] * length == password:
            length += 1
            shift = 0
        else:
            shift += 1
