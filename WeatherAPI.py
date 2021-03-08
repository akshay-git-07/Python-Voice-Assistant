import requests


def get_weather_data(city_name):
    response = requests.get(base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric")
    data = response.json()

    if data["cod"] != "404":
        weatherData = data["main"]

        name = data["name"]
        temperature = weatherData["temp"]
        feels_like = weatherData["feels_like"]

        return f'Current temperature in {name} is {temperature} degree celsius, it feels like {feels_like} degree'

    return 'Weather data not found'


api_key = 'YOUR_API KEY'
base_url = "http://api.openweathermap.org/data/2.5/weather?"


if __name__ == '__main__':
    print(get_weather_data(input('Enter city name: ')))
