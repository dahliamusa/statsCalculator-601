import statistics


def valid(data):
    for num in data:
        if type(num) == str:
            return 0
    return 1

def stats_zscore(data):
    mean_value = statistics.mean(data)
    stdev_value = statistics.stdev(data)
    result = []
    for num in data:
        result.append((num - mean_value) / stdev_value)
    return result