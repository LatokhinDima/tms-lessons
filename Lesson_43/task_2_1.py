import time
import aiohttp
import asyncio

cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

async def async_loading(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?appid=2a4ff86f9aaa70041ec8e82db64abf56&q={city}&units=metric'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(f'Температура в {city}: {data["main"]["temp"]} C')

async def main():
    tasks = [asyncio.create_task(async_loading(city)) for city in cities]
    await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f'Total time: {end_time - start_time} seconds')

