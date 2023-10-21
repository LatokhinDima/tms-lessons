my_dict = {'a': 4, 'b': 112, 'c': 78, 'd': 74}
res = 0

for key, value in my_dict.items():
    if value > res:
        res = value

print(res)
