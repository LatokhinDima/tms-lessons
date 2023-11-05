import json
a = input('Enter your name: ')
b = input('Enter your surname: ')
c = input('Enter your age: ')
data = {'name': a, 'surname': b, 'age': c}
with open('file_04.json', 'w') as file:
     json.dump(data, file)
