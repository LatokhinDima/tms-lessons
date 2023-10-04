def generate_natural_cubes(n: int) -> list:
    return [i ** 3 for i in range(1, n + 1)]

print(generate_natural_cubes(6))
