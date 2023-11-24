from test import test_sort
import copy


def bubble_sort(lst: list) -> list:
    lst = copy.deepcopy(lst)
    a = len(lst)
    for i in range(a):
        for j in range(0, a - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == '__main__':
    test_sort(bubble_sort)
