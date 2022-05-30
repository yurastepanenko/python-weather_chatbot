from datetime import datetime
from pprint import pprint

import requests
from config import open_weather_token



def get_weather(city, open_weather_token):

    try:
        # наш запрос
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}',
            params={"units": "metric"})
        data = r.json()
        pprint(data)



    except Exception as ex:
        print(ex)


def main():
    city = input('Введите город для получения погоды: ')
    get_weather(city, open_weather_token)


if __name__ == "__main__":
    main()
