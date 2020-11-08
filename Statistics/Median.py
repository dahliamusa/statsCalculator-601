def median(data):
    num_values = len(data)
    data.sort()
    if num_values % 2 == 0:
        median1 = int(data[num_values // 2])
        median2 = int(data[num_values // 2 - 1])
        return (median1 + median2) / 2
    else:
        return data[num_values // 2]