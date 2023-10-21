def filter_negative_numbers(num):
    return list(filter(lambda x: x >= 0, num))

print(filter_negative_numbers([6, -5, 0, -1, 100]))
