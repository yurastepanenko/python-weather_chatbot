from pprint import pprint

import requests
import datetime
from config import open_weather_token, telegam_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from constans import EMOJIS
import markups as nav

bot = Bot(token=telegam_token)
dp = Dispatcher(bot)
kurs_list = requests.get(
            f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json')
data_kurs = kurs_list.json()
pprint(data_kurs)
print(len(data_kurs))

new_cur = []
for _ in data_kurs:
 if _['r030']in(840,978,826):
  new_cur.append(_)

print(new_cur)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет, напиши название города и получишь погоду!', reply_markup=nav.mainMenu)


async def get_time(message:types.Message):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}',
            params={"units": "metric"})
        data = r.json()
        print(data)
        await message.reply(
            f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n')

    except:
        await message.reply('\u2620Проверьте название города\u2620')

@dp.message_handler()
async def get_weather(message:types.Message):
    if message.text == 'Получить Время':
        await get_time(message)
    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)
    elif message.text == 'Другое':
        await bot.send_message(message.from_user.id, 'Другое', reply_markup=nav.otherMenu)
    elif message.text == 'Информация':
        await bot.send_message(message.from_user.id, 'Разработал Степаненко Юрий. Июнь -2022. Версия - 1.')
    elif message.text == 'Курс Валют':
        # await bot.send_message(message.from_user.id, data_kurs[0:3])
        await message.reply(f'Курс доллара = {new_cur[1]["rate"]},\nКурс Евро = {new_cur[2]["rate"]},\nКурс Фунтов = {new_cur[0]["rate"]}')
    else:

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
