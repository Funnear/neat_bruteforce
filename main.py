import sys

from src import config
from src.method import Method
from src.brute_force import brute_force
from src.common_password_generator import common_password_generator
from src.pickup_common import PickupCommon
from src.password_generator import password_generator
from src.user_data import user_data
from src.user_specific_credential_generator import user_specific_credential_generator


def main(**kwargs):
    if kwargs.keys().__contains__('method'):
        method_id = int(kwargs['method'])
        method = Method(method_id)
    else:
        method = Method(1)

    if kwargs.keys().__contains__('username'):
        username = kwargs['username']
    else:
        username = config.get('login')

    if kwargs.keys().__contains__('passwords_limit'):
        passwords_limit = kwargs['passwords_limit']
    else:
        passwords_limit = 10000

    if method is Method.COMMON and passwords_limit == 10000:
        file_path = 'resources/10k-most-common.txt'
    elif method is Method.COMMON and passwords_limit == 1000000:
        file_path = 'resources/10-million-password-list-top-1000000.txt'
    elif method is Method.COMMON:
        raise AttributeError('Pick-up Common algorithm supports only 10,000 or 1,000,000 passwords limit.')

    if method is Method.COMMON and kwargs.keys().__contains__('iterator'):
        passwords = PickupCommon(file_path)
    elif method is Method.COMMON:
        passwords = common_password_generator(file_path)

    if method is Method.ALPHABET:
        passwords = password_generator()

    if method is Method.USERDATA:
        user = user_data()
        passwords = user_specific_credential_generator(user)

    if kwargs.keys().__contains__('generate_usernames'):
        username = passwords

    brute_force(username, passwords, passwords_limit)


if __name__ == "__main__":
    count_args = len(sys.argv)
    if count_args > 0:
        main(**dict(arg.split('=') for arg in sys.argv[1:]))
    else:
        main()
