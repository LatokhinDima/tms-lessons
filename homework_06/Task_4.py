from functools import reduce


def my_join(string, separator):
    return reduce(lambda x, y: x + separator + y, string)


words = input('Enter words (use space):  ').split()
separator = input('Enter separator: ')

print(my_join(words, separator))
