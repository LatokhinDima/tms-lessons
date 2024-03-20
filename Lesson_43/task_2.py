import time
import requests

cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']


def sync_loading():
    for city in cities:
        url = 'https://api.openweathermap.org/data/2.5/weather' \
              f'?appid=2a4ff86f9aaa70041ec8e82db64abf56&q={city}&units=metric'
        response = requests.get(url).json()
        print(f'Температура в {city}: {response["main"]["temp"]} C')


start_time = time.time()
sync_loading()
end_time = time.time()
print(f'Total time: {end_time - start_time} seconds')
