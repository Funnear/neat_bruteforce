from collections import Iterable
from types import GeneratorType


def credentials_pair_generator(usernames, passwords):
    """

    :type usernames: list, generator or iterable object
    :type passwords: generator or iterable object
    """
    passwords = iter(passwords)
    while True:
        try:
            if isinstance(usernames, GeneratorType) or isinstance(usernames, Iterable):
                username = usernames.__next__()
            elif len(usernames) == 1:
                username = usernames[0]
            else:
                try:
                    usernames = iter(usernames)
                    username = usernames.__next__()
                except AttributeError:
                    raise AttributeError(f'Refactor usernames type. Passed usernames: {usernames}')

            while True:
                try:
                    password = passwords.__next__()
                    yield username, password
                except StopIteration:
                    break
        except StopIteration:
            break
