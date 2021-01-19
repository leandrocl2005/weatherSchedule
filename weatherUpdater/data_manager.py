import requests
from weather.models import Weather


def _get_weather_json():
    url = 'https://api.hgbrasil.com/weather?'
    url += 'key=YOU_KEY'
    url += '&woeid=455916'

    r = requests.get(url)

    try:
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(e)
        return None


def update_weather():
    json = _get_weather_json()
    print(json['results']['forecast'][0])
    if json is not None:
        try:
            new_wheather = Weather()

            new_wheather.temperature = json['results']['temp']
            new_wheather.description = json['results']['description']
            new_wheather.date = json['results']['date']
            new_wheather.time = json['results']['time']

            new_wheather.save()

        except Exception as e:
            print(e)
            pass
