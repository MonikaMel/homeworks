import requests
import json

moscow = requests.get("https://api.weather.yandex.ru/v2/forecast?lat=55.751244&lon=37.618423&limit=5",
                 headers={'X-Yandex-API-Key': "7f1ad213-842a-4d42-8c54-dd1b9e5c999e"})

berlin = requests.get("https://api.weather.yandex.ru/v2/forecast?lat=52.520008&lon=13.404954&limit=5",
                 headers={'X-Yandex-API-Key': "7f1ad213-842a-4d42-8c54-dd1b9e5c999e"})

rome = requests.get("https://api.weather.yandex.ru/v2/forecast?lat=41.902782&lon=12.496366&limit=5",
                 headers={'X-Yandex-API-Key': "7f1ad213-842a-4d42-8c54-dd1b9e5c999e"})

data = {}


def get_weather_forecast(response):
    string_js = response.text
    json_acceptable_string = string_js.replace("'", "\"")
    data = json.loads(json_acceptable_string)
    var = data['forecasts']
    return var


data['moscow'] = get_weather_forecast(moscow)
data['berlin'] = get_weather_forecast(berlin)
data['rome'] = get_weather_forecast(rome)


with open('weather_forecast.json', 'w') as file:
    json.dump(data, file, indent=4)





