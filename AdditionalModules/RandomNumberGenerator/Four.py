from random import randrange
from random import seed
from time import time


def four(data):
    seed(time())
    return data[randrange(len(data))]