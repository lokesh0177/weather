import requests
api_key = 'd285db9e5a801f031bf4156ae5137a8f'

user_input = input("Enter city:")

data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if data.status_code == '404':
    print("No City Found")
else:
    weather_data = data.json()['weather'][0]['main']
    temp = data.json()['main']['temp']
    print(f"Ther weather in {user_input} is {weather_data}")
    print(f"The Temperature in {user_input} is {temp}ºF")