def is_year_leap2(year: int) -> bool:
    if year % 4 == 0:
        return True
    else:
        return False


print(is_year_leap2(1700))
