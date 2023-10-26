import csv

with open('file_07.csv', 'r') as file:
    file_reader = csv.reader(file, delimiter=',')
    index = 0
    for row in file_reader:
        if index != 0:
          print(row[1], row[0], row[2])
        index += 1
