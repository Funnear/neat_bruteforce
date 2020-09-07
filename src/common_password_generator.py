import resource


def common_password_generator(file_path):
    try:
        input_file = open(file_path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f'Invalid path to passwords file: {file_path}')

    newline = input_file.readline()
    while newline:

        # mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # print(mem_usage)

        yield newline.strip('\n')
        newline = input_file.readline()

    input_file.close()
