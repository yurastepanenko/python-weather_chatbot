import requests
import datetime
from config import open_weather_token, telegam_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=telegam_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет, напиши название города и получишь погоду!')


if __name__ == '__main__':
    executor.start_polling(dp)