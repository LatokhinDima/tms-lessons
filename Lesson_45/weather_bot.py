import asyncio
import logging
import sys
import aiohttp
from os import getenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton

TOKEN = getenv("TELEGRAM_BOT_TOKEN")

dp = Dispatcher()
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

MINSK_WEATHER_KEY = 'minks_weather'


async def get_weather(city=None, lat=None, lon=None) -> float:
    url = 'https://api.openweathermap.org/data/2.5/weather' \
          '?appid=2a4ff86f9aaa70041ec8e82db64abf56&units=metric'
    if city is not None:
        url += f'&q={city}'
    elif lat is not None and lon is not None:
        url += f'&lat={lat}&lon={lon}'
    else:
        raise Exception('city or lat/lon must be specified')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather_json = await response.json()
            return weather_json['main']['temp']


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = [[KeyboardButton(text='Get weather', request_location=True)]]
    await message.answer(f"Hello, I'm weather bot. I can say you weather in your location!",
                         reply_markup=types.ReplyKeyboardMarkup(keyboard=keyboard))


@dp.message(F.location)
async def echo_handler(message: Message) -> None:
    temperature = await get_weather(lat=message.location.latitude,
                                    lon=message.location.longitude)
    await message.answer(f'Weather at your location: {temperature}°C')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(dp.start_polling(bot))
