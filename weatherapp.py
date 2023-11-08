import requests
import json
import time

API_KEY = "9475256e5c164e7fb71172005230811"

def get_weather_data(city):
    url :"http://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=yes".format(API_KEY, city)
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        raise Exception("API request failed")
    
def print_weather_data(data):
    print("City : {}".format(data["location"]["name"]))
    print("Temperature : {} degree C".format(data["current"]["temp_c"]))
    print("Temperature : {} degree F".format(data["current"]["temp_f"]))
    print("Humidity : {}%".format(data["current"]["humidity"]))
    print("Wind speed : {}m/h".format(data["current"]["wind_mph"]))
    print("Wind speed : {}km/h".format(data["current"]["wind_kmph"]))
    print("Wind direction : {}".format(data["current"]["wind_dir"]))

#create
print("Please enter list of cities with spaces in between")
favourite_cities = [i for i in input().split()]
print(favourite_cities)

data_validation = False

while data_validation == False:
    city = input("please enter the city name: ")
    try:
        for character in city:
            if character.isalpha():
                data_validation = True
    except:
        print("only city names are accepted")
        break;

#outcomes
if data_validation == True:
    weather_data = get_weather_data(city)
    print_weather_data(weather_data)

def add_city(city):
    favourite_cities.append(city)

def remove_city(city):
    favourite_cities.remove(city)

def update_city(city, new_data):
    for index, item in enumerate(favourite_cities):
        if item == city:
            favourite_cities[index] = new_data
            break

while True:
    if data_validation == True:
        weather_data = get_weather_data(city)
        time.sleep(30)

