from random import randrange
from random import seed


def seven(data, n, seed_value):
    seed(seed_value)
    result = []
    for x in range(0, n):
        result.append(data[randrange(0, len(data))])
    return result