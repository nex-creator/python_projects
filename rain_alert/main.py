import os


import requests

API_KEY= os.environ.get("OWN_API_KEY")
MY_LAT = 42.332939
MY_LONG = -83.047836
OWN_ENDPOINT= "https://api.openweathermap.org/data/2.5/forecast"

weather_parameters  ={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt":4,

}

response = requests.get(url=OWN_ENDPOINT, params= weather_parameters)

#raise any exception if unsuccessfull
response.raise_for_status()
print(response.status_code)
#get json data
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code= (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.")

