import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram import executor


API_TOKEN = "7081612419:AAERcE3rQpvS6h84LzNkI4_Th6xHAWSQ8fk"  # Получите API токен для вашего бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)


def get_weather(city):
    api_key = "90fcf792156443467cd4d267ebf720ab"  # Получите свой API ключ на сайте OpenWeatherMap
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The weather in {city} is {weather_description}. Temperature: {temperature}K"
    else:
        return "Error fetching weather data"


@dp.message_handler(commands=['weather'])
async def send_weather(message: Message):
    city = "Minsk"
    weather_info = get_weather(city)
    await message.answer(weather_info)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
