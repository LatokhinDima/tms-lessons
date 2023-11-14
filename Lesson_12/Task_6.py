def generate_squares(count):
    for i in range(1, count + 1):
        yield i ** 2

for i in generate_squares(10):
    print(i)
