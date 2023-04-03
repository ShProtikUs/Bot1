from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

API_TOKEN = '6009417059:AAGAMDDMP8EfQOYRU4-1y1vcUdh6ulg9xUo'

WEBHOOK_HOST = 'https://991e-79-133-113-122.eu.ngrok.io'
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 80

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(dp):
    print('Starting...')
    await bot.set_webhook(WEBHOOK_URL)
    print('Webhook set!')


async def on_shutdown(dp):
    print('Setting down...')
    await bot.delete_webhook()
    print('Webhook deleted')


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    return SendMessage(chat_id=msg.chat.id, text='Привет! Я бот, который работает благодаря webhook!')


@dp.message_handler(commands=['help'])
async def helps(msg: types.Message):
    return SendMessage(chat_id=msg.chat.id, text='Я умный бот, который может помочь вам с какой-то проблемой!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=False,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )
