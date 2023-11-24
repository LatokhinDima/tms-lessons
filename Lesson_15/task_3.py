from test import test_sort
import copy


def insertion_sort(lst: list) -> list:
    lst = copy.deepcopy(lst)
    a = len(lst)
    for i in range(1, a):
        x = lst[i]
        j = i

        while j > 0 and lst[j - 1] > x:
            lst[j] = lst[j - 1]
            j -= 1

    return lst


if __name__ == '__main__':
    test_sort(insertion_sort)
