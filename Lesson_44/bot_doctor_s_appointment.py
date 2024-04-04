import asyncio
import logging
import sqlite3
import sys
from os import getenv


from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup



# Подключение к базе данных SQLite
conn = sqlite3.connect('appointments.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                    date TEXT,
                    time TEXT,
                    user_id INTEGER
                )''')
conn.commit()

TOKEN = getenv("TELEGRAM_BOT_TOKEN")

dp = Dispatcher()
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


#Обработчик команды /start
@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("Привет! Я бот для записи на прием. Используйте команду /appoint для записи.")

# Обработчик кнопок с выбором даты и времени
@dp.callback_query(lambda query: query.data.startswith('appointment'))
async def process_appointment(callback_query: types.CallbackQuery):
    data = callback_query.data.split('_')
    date = data[1]
    time = data[2]
    user_id = callback_query.from_user.id

    # Проверяем, свободен ли выбранный слот времени
    cursor.execute("SELECT * FROM appointments WHERE date=? AND time=?", (date, time))
    if cursor.fetchone():
        await bot.answer_callback_query(callback_query.id, "Это время уже занято.")
    else:
        cursor.execute("INSERT INTO appointments (date, time, user_id) VALUES (?, ?, ?)", (date, time, user_id))
        conn.commit()
        await bot.answer_callback_query(callback_query.id, f"Вы записаны на {date} в {time}.")

# Генерация кнопок выбора даты и времени
def generate_appointment_buttons():
    markup = InlineKeyboardMarkup()
    for date in ['2022-01-01', '2022-01-02', '2022-01-03']:  # Замените на реальные даты
        for time in ['10:00', '12:00', '14:00', '16:00', '18:00']:  # Замените на реальные время
            markup.row(InlineKeyboardButton(f'{date} {time}', callback_data=f"appointment_{date}_{time}"))
    return markup

# Обработчик команды /appoint
@dp.message(Command('appoint'))
async def appoint(message: types.Message):
    await message.answer("Выберите день и время для записи:", reply_markup=generate_appointment_buttons())

# Запуск бота
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(dp.start_polling(bot))
