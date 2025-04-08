import logging
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# Загрузим переменные из .env
load_dotenv()

# Получаем токен для бота и API-ключ OpenAI из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Настройка OpenAI
openai.api_key = OPENAI_API_KEY

# Настройка бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Логирование
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я GPT-бот. Напиши что-нибудь, и я отвечу.")

@dp.message_handler()
async def handle_message(message: types.Message):
    # Запрашиваем ответ от GPT
    response = openai.Completion.create(
        engine="text-davinci-003",  # Можно использовать другой двигатель
        prompt=message.text,
        max_tokens=150
    )

    # Отправляем ответ в чат
    await message.reply(response.choices[0].text.strip())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
