from ctypes.wintypes import LONG
import requests  # a request for any data e.g. an API


API_KEY = "61c481999b6ad2a9f420ee3fb0abaea0"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# We need to get Latitude and Longitud from the specified city with a second API for greater accuracy
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"  # f strings are for ^3.6.0 and allow you to interpolate strings

response = requests.get(
    request_url
)  # This is a kind off HTTP request; also important the status code

if response.status_code == 200:  # means satisfactory code
    data = response.json()
    weather = data["weather"][0][
        "description"
    ]  # [0] to access inside the array of the dictionary
    print(
        "Weather:", weather.capitalize()
    )  # prints out all the data but we can access the preferred sections like this:
    # weather = data['weather']
    # Important note: if it is subdictionaried, we must place the path
    temperature = round(
        data["main"]["temp"] - 273.15, 2
    )  # 2 defines the decimals' length
    maxTemperature = round(data["main"]["temp_max"] - 273.15, 2)
    minTemperature = round(data["main"]["temp_min"] - 273.15, 2)
    humidity = data["main"]["humidity"]
    print("Temperature:")
    print(temperature, " ºC")
    print("Maximum temperature:")
    print(maxTemperature, " ºC")
    print("Minimum temperature:")
    print(minTemperature, " ºC")
    print("Humidity:")
    print(humidity, " %")

else:
    print("An error occurred.")
