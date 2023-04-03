import asyncio, os

from aiogram import Bot, Dispatcher, types

API_KEY = '6009417059:AAGAMDDMP8EfQOYRU4-1y1vcUdh6ulg9xUo'
bot = Bot(token=API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    print(msg.text)
    await bot.send_message(chat_id=msg.chat.id, text='Привет', reply_to_message_id=msg.message_id)


@dp.message_handler(commands=['help'])
async def helps(msg: types.Message):
    print(msg.text)
    await bot.send_message(chat_id=msg.chat.id, text='Я умный бот, который может писать Привет',
                           reply_to_message_id=msg.message_id)


async def main():
    await dp.start_polling(timeout=3)

if __name__ == '__main__':
    asyncio.run(main())