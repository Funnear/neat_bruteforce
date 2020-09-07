from enum import Enum, unique


@unique
class Method(Enum):
    COMMON = 1
    ALPHABET = 2
    USERDATA = 3
