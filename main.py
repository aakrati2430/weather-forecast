import requests

API_KEY = "17f4575672c294ebd9d53d1c5f7885c9"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = F"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else: 
        return None

def display_weather(data):
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    min_temp =data['main']['temp_min']
    max_temp = data['main']['temp_max'] 
    print(f"weather in {data['name']}:{weather}")
    print(f"tempreture : {temperature}")
    print(f"range of tempreture is = {min_temp} -{max_temp}")


city = input("please tell your city")

weatherdata = get_weather(city)
 

if weatherdata:
    display_weather(weatherdata)
else:
    print('city is not defind')    




        
