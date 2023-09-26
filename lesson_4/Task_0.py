summ = 0
for a in range(1, 101):
    summ +=a
print(f'1: {summ}')

summ_1 = 0
for a in range(100, 1001):
    summ_1 +=a
print(f'2: {summ_1}')

summ_2 = 0
for a in range(100, 1001, 2):
    summ_2 +=a
print(f'3: {summ_2}')

umn_1 = 1
for a in range(1, 11):
    umn_1 *= a
print(f'4: {umn_1}')

mn = 2
for _ in range(1, 10):
    mn *= 2
print(f'5: {mn}')

summ_3 = 0
i = 0
while summ_3 <= 1000:
    i += 1
    summ_3 += i


print(f'6: {summ_3} {i}')






