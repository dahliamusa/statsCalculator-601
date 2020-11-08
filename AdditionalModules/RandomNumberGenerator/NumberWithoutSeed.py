from random import randrange
from random import seed
from time import time


def num_without_seed(low, high):
    seed(time())
    number = randrange(low, high)
    if randrange(0, 2) == 0:
        decimal = randrange(1, 99)
        string = str(number) + "." + str(decimal)
        return float(string)
    else:
        return number
