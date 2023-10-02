import random

number = random.randint(0, 100)

while True:
    answer = int(input('Enter number:  '))
    if number == answer:
        print('You win!')
        break
    elif number < answer:
        print('не угадал, число больше загаданного')
    else:
        print('не угадал, число меньше загаданного')
