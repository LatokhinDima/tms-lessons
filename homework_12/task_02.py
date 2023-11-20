import re


def is_date(string: str) -> bool:
    return re.fullmatch(r'\d{2}-\d{2}-\d{4}', string) is not None


assert not is_date('253-053-2016')
assert not is_date('37-UU-1000')
assert is_date('01-01-0000')
assert is_date('27-53-2028')
