from datetime import datetime
from pprint import pprint
import json
import requests
from config import open_weather_token



def get_weather(city, open_weather_token):
    """Процедура получает по АПИ погоду(токен мы зарегили заранее)
    Парсит ответ в виде джейсона и возвращает пользователю"""
    try:
        # r- наш запрос "units": "metric" - для того чтобы получить в цельсиях,
        # а не в Кельвинах
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}',
            params={"units": "metric"})
        data = r.json()
        #pprint(data)

        city = data['name']
        weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        # рассвет
        sunrise_timestamp = datetime.fromtimestamp(data['sys']['sunrise'])
        # закат
        sunset_timestamp = datetime.fromtimestamp(data['sys']['sunset'])

        pprint(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
              f'Погода в городе {city}\n'
              f'Температура: {weather}\u2103\n'
              f'Влажность: {humidity}%\n'
              f'Давление: {pressure} мм.рт.ст.\n'
              f'Ветер: {wind}м/с\n'
              f'Восход солнца: {sunrise_timestamp}\n'
              f'Закат солнца: {sunset_timestamp}\n')
              # f'Продолжительность дня {len_of_day}\n'



    except Exception as ex:
        print(ex)


def main():
    """
        Основная процедура, которая запускает нашу программу
    """
    city = input('Введите город для получения погоды: ')
    get_weather(city, open_weather_token)


if __name__ == "__main__":
    main()
