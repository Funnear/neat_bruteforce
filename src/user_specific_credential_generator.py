from itertools import product

from src import config
from src.letter_replace import letter_replace


def user_specific_credential_generator(user):
    dataset = list()
    dataset.append(user['email'].lower())
    dataset.append(user['name'].lower())
    dataset.append(user['surname'].lower())

    email_parsed = user['email'].split('@')
    email_parsed.append(email_parsed[1].split('.')[0])
    email_parsed.append(email_parsed[1].split('.')[1])
    for item in email_parsed:
        dataset.append(item)

    dataset_freeze = list(dataset)
    for item in dataset_freeze:
        dataset.append(item.upper())
        dataset.append(item.title())

    dataset_freeze = list(dataset)
    for item in dataset_freeze:
        dataset.append(letter_replace(item))

    birth_date_parsed = user['birth_date'].split('.')
    for item in birth_date_parsed:
        dataset.append(item)

    length = int(config.get('minimal_password_length'))
    dataset.sort()
    for n in range(1, len(dataset)):
        combinations = product(dataset, repeat=n)
        for combination in combinations:
            password = ''
            for particle in combination:
                password += particle
            if len(password) < length:
                pass
            else:
                yield password
