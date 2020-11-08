from random import randrange
from random import seed
from time import time


def random_item(data):
    seed(time())
    return data[randrange(0, len(data))]