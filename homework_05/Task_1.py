def is_year_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

print(is_year_leap(2200))
print(is_year_leap(2020))
print(is_year_leap(800))
print(is_year_leap(2012))
print(is_year_leap(1700))
