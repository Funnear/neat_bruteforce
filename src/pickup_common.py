import resource


class PickupCommon:
    def __init__(self, file_path):
        try:
            with open(file_path) as f:
                self.passwords = f.readlines()
                self.index = 0
        except FileNotFoundError:
            raise FileNotFoundError(f'Invalid path to passwords file: {file_path}')

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.index < len(self.passwords):
            password = self.passwords[self.index].strip('\n')
            self.index += 1

            # mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            # print(mem_usage)

            return password
        else:
            raise StopIteration()
