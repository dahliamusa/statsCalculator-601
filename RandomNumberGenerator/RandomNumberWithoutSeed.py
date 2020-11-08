from random import randrange


def num_without_seed(low, high):
    number = randrange(low, high)
    if randrange(0, 2) == 0:
        decimal = randrange(1, 99)
        string = str(number) + "." + str(decimal)
        return float(string)
    else:
        return number
