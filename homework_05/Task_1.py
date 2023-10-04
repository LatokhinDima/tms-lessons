def is_year_leap(year: int) -> bool:
    if year % 100 != 0 and (year % 400 == 0 or year % 4 == 0):
        return True
    else:
        return False

print(is_year_leap(2200))
print(is_year_leap(2020))
print(is_year_leap(800))
print(is_year_leap(2012))
