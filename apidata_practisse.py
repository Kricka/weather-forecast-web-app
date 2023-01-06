import requests

url="http://api.weatherapi.com/v1/forecast.json?key=3a622c885a0f4452960101835230601 &q=London&days=5&aqi=no&alerts=no"

response=requests.get(url)

data=response.json()

day=[]
temperature=[]

for days in data['forecast']['forecastday']:
    day.append(days['date'])

for temp in data['forecast']['forecastday']:
    temperature.append(temp['day']['avgtemp_c'])

"""
url="http://api.weatherapi.com/v1/forecast.json?key=3a622c885a0f4452960101835230601 &q=Belgrade&days=5&aqi=no&alerts=no"

response=requests.get(url)

data=response.json()

day=[]
temperature=[]

for days in data['forecast']['forecastday']:
    day.append(days['date'])

for temp in data['forecast']['forecastday']:
    temperature.append(temp['day']['avgtemp_c'])
"""