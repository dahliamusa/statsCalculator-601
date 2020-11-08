from math import pow
from Statistics.Mean import mean
from Calculator.Addition import addition


def variance(data):
    mean_value = mean(data)
    terms = [pow((reading - mean_value), 2) for reading in data]
    total = 0
    for num in terms:
        total = addition(total, num)
    return total / float(len(data) - 1)