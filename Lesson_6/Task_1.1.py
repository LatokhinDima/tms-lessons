def input_list():
    s = input('Enter string:   ').split()
    return list(map(lambda x: int(x), s))


my_list = input_list()
print(my_list)
