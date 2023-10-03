def input_list():
    s = input('Enter string:   ').split()
    return list(map(lambda x: int(x), s))

my_list = list(map(lambda a: round(a / 100), input_list()))
print(my_list)
