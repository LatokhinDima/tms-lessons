import re


def is_phone_number(string):
    return re.fullmatch('\+\d{3}\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}', string) is not None

assert is_phone_number('+375 (44) 729-65-53')
assert not is_phone_number('-658 58 66')
