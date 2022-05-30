import requests
import datetime
from config import open_weather_token, telegam_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from constans import EMOJIS


bot = Bot(token=telegam_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет, напиши название города и получишь погоду!')


@dp.message_handler()
async def get_weather(message:types.Message):

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}',
            params={"units": "metric"})
        data = r.json()

        weather_description = data['weather'][0]['main']
        if weather_description in EMOJIS:
            wd = EMOJIS[weather_description]
        else:
            print('ХМ! Что-то необычное, у нас пока нет такого EMOJI :(((')

        city = data['name']
        cur_weather = data['main']['temp']
        cur_humidity = data['main']['humidity']
        cur_pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        len_of_day = sunset_timestamp - sunrise_timestamp
        await message.reply(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
              f'Погода в городе {city}\nТемпература: {cur_weather} {wd}\u2103\n'
              f'Влажность: {cur_humidity}%\nДавление: {cur_pressure}мм.рт.ст.\n'
              f'Ветер: {wind}м/с\nВосход солнца: {sunrise_timestamp}\n'
              f'Закат солнца: {sunset_timestamp}\n'
              f'Продолжительность дня {len_of_day}\n'
              f'Хорошего дня!')

    except:
        await message.reply('\u2620Проверьте название города\u2620')


if __name__ == '__main__':
    executor.start_polling(dp)
