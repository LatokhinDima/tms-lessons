with open('file_02.txt', 'w') as file:
    file.write('First line\n')
    file.write('Second line\n')
    file.write('Third line\n')

with open('file_02.txt', 'r') as file:
    for line in file:
        print(line)
