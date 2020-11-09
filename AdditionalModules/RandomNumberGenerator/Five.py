from random import randrange
from random import seed


def five(data, seed_value):
    seed(seed_value)
    return data[randrange(0, len(data))]