import csv
header = ('name', 'surname', 'gender')
content = [('Dmitry', 'Latokhin', 'M')]

with open('file_06.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    for content in content:
        writer.writerow(content)

