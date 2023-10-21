
my_dict = {'a': 4, 'b': 12, 'c': 99, 'd': 74}
max_val = None
res = None

for key, value in my_dict.items():
    if max_val is None or value > max_val:
        max_val = value
        res = key

print(res)
