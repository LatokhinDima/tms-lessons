def my_decorator(func):
    def decor(x):
        print(f'input parameter:  {x}')
        y = func(x)
        print(f'result:  {y}')
        return y
    return decor


@my_decorator
def my_func(x):
    return x ** 2


y = my_func(6)
print(f'y = {y}')
