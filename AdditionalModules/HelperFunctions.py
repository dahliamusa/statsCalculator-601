import statistics


def stats_zscore(data):
    mean_value = statistics.mean(data)
    stdev_value = statistics.stdev(data)
    result = []
    for num in data:
        result.append((num - mean_value) / stdev_value)
    return result