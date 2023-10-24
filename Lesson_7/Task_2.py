import json

data = {'name': 'Dmitry', 'surname': 'Latokhin'}
with open('file_03.json', 'w') as file:
     json.dump(data, file)
