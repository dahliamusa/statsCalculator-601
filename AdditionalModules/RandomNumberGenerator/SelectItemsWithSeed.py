from random import randrange
from random import seed


def select_items_with_seed(data, n, seed_value):
    seed(seed_value)
    result = []
    for x in range(0, n):
        result.append(data[randrange(0, len(data))])
    return result