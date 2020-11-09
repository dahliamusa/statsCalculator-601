from random import randrange
from random import seed


def three(length, seed_value):
    seed(seed_value)
    result = []
    for x in range(0, length):
        number = randrange(0, 1000)
        if randrange(0, 2) == 0:
            decimal = randrange(1, 100)
            string = str(number) + "." + str(decimal)
            result.append(float(string))
        else:
            result.append(number)
    return result
