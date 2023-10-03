from functools import reduce

def input_list():
    s = input('Enter string:   ').split()
    return list(map(lambda x: int(x), s))


my_list = reduce(lambda a, b: a + b, input_list(), 1)
print(my_list)
