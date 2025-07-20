import os
import asyncio
from aiogram import Bot, Dispatcher, types

API_TOKEN = os.getenv('BOT_TOKEN')

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Пример обработчика команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я эхо-бот на aiogram.")

# Эхо-обработчик
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# Запуск бота
async def main():
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
