from collections import Counter


def mode(data):
    count = Counter(data)
    count_list = dict(count)
    max_value = max(list(count.values()))
    mode_val = [num for num, freq in count_list.items() if freq == max_value]
    if len(mode_val) == len(data):
        raise Exception("No mode found")
    else:
        result = list(map(str, mode_val))
        return int(result[0])

