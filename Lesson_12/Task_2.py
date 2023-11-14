import re


def is_car_number(string):
    return re.fullmatch('\d{4}[A-Z]{2}-\d', string) is not None

assert is_car_number('2536GH-3')
assert not is_car_number('2536jbdsfbks')
assert not is_car_number('2536АП-3')

#print(is_car_number('2536GH-3'))
#print(is_car_number('2536jbdsfbks'))
#print(is_car_number('2536АП-3'))


