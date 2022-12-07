import requests

api_key = 'eee602db914245263bcfa0da85dcbb8c'
ruwanwella_latitude = 7.045873
ruwanwella_longitude = 80.253706

#url = f'https://api.openweathermap.org/data/3.0/onecall?lat={ruwanwella_latitude}&lon={ruwanwella_longitude}&appid={api_key}&units=metric'
url = f'https://api.openweathermap.org/data/2.5/weather?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={api_key}'

#url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q=colombo'

response = requests.request('get', url=url).json()

with open('weather_data.json', 'w') as file:
    file.write(str(response))

for i in response:
    print(i, response[i])
