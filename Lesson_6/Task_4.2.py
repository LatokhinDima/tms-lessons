from functools import reduce

def input_list():
    s = input('Enter string:   ').split()
    return list(map(lambda x: int(x), s))


my_list = reduce(lambda a, b: min(a, b), input_list())
print(my_list)
