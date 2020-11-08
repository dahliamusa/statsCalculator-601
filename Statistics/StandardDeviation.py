from math import pow
from Statistics.Variance import variance


def stdev(data):
    return pow(variance(data), 0.5)