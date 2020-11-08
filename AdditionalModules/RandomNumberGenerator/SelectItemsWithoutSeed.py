from random import randrange
from AdditionalModules.RandomNumberGenerator.RandomItem import random_item


def select_items(data, n):
    result = []
    for x in range(0, n):
        result.append(random_item(data))
    return result