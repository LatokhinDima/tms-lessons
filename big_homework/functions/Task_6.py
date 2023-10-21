#Function_Task_1
def hello_world():
    print('Hello world!')

#Function_Task_2
def my_sum(x, y):
    return x + y

#Function_Task_3
def simple_compare(x, y):
    if x < y:
        return 'True'
    else:
        return 'False'

#Function_Task_4
def compare(x, y):
    if x < y:
        return -1
    if x > y:
        return 1
    if x == y:
        return 0

#Function_Task_5
def filter_negative_numbers(num):
    return list(filter(lambda x: x >= 0, num))

#Realization_Task_6
number = int(input('Введите номер задачи: '))
if number == 1:
    hello_world()
elif number in (2, 3, 4):
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    if number == 2:
        print(f'Сумма чисел: {my_sum(x, y)}')
    elif number == 3:
        print(f'Первое число меньше второго? Ответ: {simple_compare(x, y)}')
    else:
        print(f'Результат сравнения: {compare(x, y)}')
elif number == 5:
    user_list = list(map(int, input('Введите числа, разделённые пробелом  ').split()))
    #user_list = [int(i) for i in input('Введите числа разделенные пробелом  ').split()]
    print(f'Мы удалили отрицательные числа из вашего списка: {filter_negative_numbers(user_list)}')
else:
    print('Задачи с таким номером нет.')
