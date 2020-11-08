from Statistics.Mean import mean
from Statistics.StandardDeviation import stdev


def zscore(data):
    mean_value = mean(data)
    stdev_value = stdev(data)
    result = []
    for num in data:
        result.append((num - mean_value) / stdev_value)
    return result
