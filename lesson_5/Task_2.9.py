def get_natural_numbers(n: int) -> list:
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers


print(get_natural_numbers(52))
