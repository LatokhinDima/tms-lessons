import re


def is_float_number(string: str) -> bool:
    return re.fullmatch(r'\d+\.\d+', string) is not None


assert is_float_number('7.5')
assert is_float_number('852369543332.0662')
assert is_float_number('6.62')
assert not is_float_number('1,j3')
assert not is_float_number('12')
assert not is_float_number('I.52')
