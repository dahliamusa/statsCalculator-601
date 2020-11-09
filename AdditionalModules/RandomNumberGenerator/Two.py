from random import randrange
from random import seed


def two(low, high, seed_value):
    seed(seed_value)
    number = randrange(low, high)
    if randrange(0, 2) == 0:
        decimal = randrange(1, 99)
        string = str(number) + "." + str(decimal)
        return float(string)
    else:
        return number