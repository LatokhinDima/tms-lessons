import csv

a = input('Enter your name: ')
b = input('Enter your surname: ')
c = input('Enter your age: ')

with open('file_07.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'surname', 'age'])
    writer.writerow([a, b, c])
