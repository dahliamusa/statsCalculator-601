import statistics


def validate(data):
    if len(data) == 0:
        raise Exception("List is empty")
    for num in data:
        if type(num) == str:
            raise Exception("Data is not numeric")


def stats_zscore(data):
    mean_value = statistics.mean(data)
    stdev_value = statistics.stdev(data)
    result = []
    for num in data:
        result.append((num - mean_value) / stdev_value)
    return result
