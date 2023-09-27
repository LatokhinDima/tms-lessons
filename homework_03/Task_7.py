number = int(input('Enter number: '))
x = 0
for i in range(2, number // 2+1):
    if (number % i == 0):
        x = x+1
if (x <= 0):
    print('True')
else:
    print('False')
