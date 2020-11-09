from random import randrange


def six(data, n):
    result = []
    for x in range(0, n):
        result.append(data[randrange(0, len(data))])
    return result