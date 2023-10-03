def input_list():
    s = input('Enter string:   ').split()
    return list(map(lambda x: int(x), s))

my_list = list(filter(lambda a: a % 2 == 0, input_list()))
print(my_list)
