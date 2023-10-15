a = int(input('number 1: '))
b = int(input('number 2: '))
c = int(input('number 3: '))
d = 0

if a > 0:
    d += 1
if b > 0:
    d += 1
if c > 0:
    d += 1

print(f'positive numbers:  {d}')
