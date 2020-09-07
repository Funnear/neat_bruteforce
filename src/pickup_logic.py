from src import config
from src.password_generator import password_generator
from src.common_password_generator import common_password_generator
from src.brute_force import brute_force
from src.pickup_common import PickupCommon
from src.user_data import user_data
from src.user_specific_credential_generator import user_specific_credential_generator


def mode(mode_switch=11):
    """

    :type mode_switch: int
    """

    if mode_switch == 11:
        user = user_data()
        username = 'Ivan2002'
        passwords_limit = 1000000
        brute_force(username, user_specific_credential_generator(user), passwords_limit)

    if mode_switch == 12:
        user = user_data()
        brute_force(user_specific_credential_generator(user), user_specific_credential_generator(user), 1000000)

    elif mode_switch == 21:
        username = config.get('login')
        passwords_limit = 10000
        # file_path = 'resources/10-million-password-list-top-1000000.txt'
        file_path = 'resources/10k-most-common.txt'
        brute_force(username, common_password_generator(file_path), passwords_limit)

    elif mode_switch == 22:
        username = config.get('login')
        passwords_limit = 10000
        brute_force(username, PickupCommon(file_path), passwords_limit)

    elif mode_switch == 3:
        username = config.get('login')
        brute_force(username, password_generator(), 100000)
