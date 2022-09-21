from enum import Enum

class Values(Enum):
    one = "1"
    zero = "0"
    other = "0.05"


class NameErrors(Enum):
    WRONG_Name = "Name doesn't contain LOC."