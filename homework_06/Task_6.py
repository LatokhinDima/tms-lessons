def my_decorator(func):
    def decor(*args,**kwargs):
        print(f'input parameter:  {args} {kwargs}')
        y = func(*args,**kwargs)
        print(f'result:  {y}')
        return y
    return decor



@my_decorator
def my_func(a, b, c, d):
   return a + b + c + d

y = my_func(1, 2, d=3, c=4)
print(f'y = {y}')
