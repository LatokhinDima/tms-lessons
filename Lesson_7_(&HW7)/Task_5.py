import json
with open('file_04.json', 'r') as file:
     data = json.load(file)
     name = data['name']
     surname = data['surname']
     age = int(data['age'])
print(f'{name} {surname} {age}')
