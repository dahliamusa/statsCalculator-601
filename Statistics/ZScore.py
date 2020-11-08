from Statistics.Mean import mean
from Statistics.StandardDeviation import stdev
import statistics


def zscore(data):
    mean_value = mean(data)
    stdev_value = stdev(data)
    result = []
    for num in data:
        result.append((num - mean_value) / stdev_value)
    return result


def stats_zscore(data):
    mean_value = statistics.mean(data)
    stdev_value = statistics.stdev(data)
    result = []
    for num in data:
        result.append((num - mean_value) / stdev_value)
    return result
