# import requests
# import pyttsx3
# def get_weather(city):
#     api_key = '961e4a4bf91fec24098bc3820c4704fe'
#     url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
#     response = requests.get(url)
#     data = response.json()
#     return data
# import time
#
#
#
# def speak(text):
#     engine = pyttsx3.init()
#     # Get available voices
#     voices = engine.getProperty('voices')
#     # Set voice to female (usually index 1)
#     engine.setProperty('voice', voices[0].id)
#     engine.say(text)
#     engine.runAndWait()
# def main():
#     city = input("Enter city name: ")
#     weather_data = get_weather(city)
#     if weather_data['cod'] == 200:
#         print(f"Weather in {city}:")
#         if weather_data['main']['temp'] >= 27:
#             speak(f"It's Hot in {city}")
#             print(f"It's Hot in {city}")
#         elif weather_data['main']['temp'] >= 23 and weather_data['main']['temp'] < 27:
#             speak(f"It's normal weather in {city}")
#             print(f"It's normal in {city}")
#         elif weather_data['main']['temp']:
#             speak(f"It's cool weather in {city}")
#             print(f"It's cool in {city}")
#         time.sleep(1)
#         print(f"Temperature: {weather_data['main']['temp']}°C")
#         print(f"Humidity: {weather_data['main']['humidity']}%")
#         print(f"Description: {weather_data['weather'][0]['description']}")
#         weather_report = f"Weather in {city}: Temperature is {weather_data['main']['temp']} degrees Celsius, Humidity is {weather_data['main']['humidity']} percent, and the condition is {weather_data['weather'][0]['description']}."
#         speak(weather_report)
#     else:
#         print("Sorry, city entered is not correct...Kindly check for spelling errors....")
#         speak("Sorry, city entered is not correct...Kindly check for spelling errors....")
#
# if __name__ == "__main__":
#     main()
#
# import csv
# import matplotlib.pyplot as plt
# import pandas as pd
# class Forecast:
#     def __int__(self):
#         pass
#
#     def forecast(self,city):
#         api_key = 'c0533613aa33720b516b1ed157a094c8'
#         base_url = 'https://api.openweathermap.org/data/2.5/forecast'
#         params = {
#             'q':f'{city}',
#             'appid':api_key,
#             'units':'metric'
#         }
#
#         response = requests.get(base_url,params=params)
#
#         output = {}
#
#         if response.status_code == 200:
#             forecast_data = response.json()
#             print(f"City: {forecast_data['city']['name']}, {forecast_data['city']['country']}")
#             print("5-Day Forecast (3-hour intervals):\n")
#             for forecast in forecast_data['list']:
#                 time = forecast['dt_txt']
#                 temperature = forecast['main']['temp']
#                 weather_desc = forecast['weather'][0]['description']
#                 print(f"Time: {time}, Temp: {temperature}°C, Weather: {weather_desc}")
#
#         else:
#             print(f"Error: {response.status_code}, {response.text}")
#         forecast_list = [
#             ['Time', 'Temperature (°C)', 'Weather']
#         ]
#
#         for forecast in forecast_data['list']:
#             time = forecast['dt_txt']
#             temperature = forecast['main']['temp']
#             weather_desc = forecast['weather'][0]['description']
#             forecast_list.append([time, temperature, weather_desc])
#
#         # Save to a CSV file
#         with open('forecast_data.csv', 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerows(forecast_list)
#
#         times = [forecast['dt_txt'] for forecast in forecast_data['list']]
#         temperatures = [forecast['main']['temp'] for forecast in forecast_data['list']]
#
#         df = pd.read_csv('forecast_data.csv')
#         speak(f"Maximum temperature in {city} is {df['Temperature (°C)'].max()} ")
#         print(f"Maximum temperature in {city} is {df['Temperature (°C)'].max()} ")
#
#         # Plot the data
#         times = [forecast['dt_txt'] for forecast in forecast_data['list']]
#         days_and_times = [pd.to_datetime(t).strftime('%d %b, %H:%M') for t in times]
#
#         # Plot
#         plt.figure(figsize=(12, 6))
#         plt.plot(days_and_times, temperatures, marker='o', color='teal', label='Temperature (°C)')
#
#         plt.title('5-Day Weather Forecast', fontsize=16)
#         plt.xlabel('Date & Time', fontsize=12)
#         plt.ylabel('Temperature (°C)', fontsize=12)
#         plt.xticks(rotation=45, fontsize=8)
#         plt.legend()
#         plt.grid(True)
#         plt.tight_layout()
#         plt.show()
#
#
# f = Forecast()
# print()
# print("-----------MODIFIED VERSION WHICH SHOWS CURRENT WEATHER AS WELL AS COMING 5 DAYS WEATHER FROM TODAY------------")
# print()
# cty = input("City: ")
# f.forecast(cty)


import requests
import pyttsx3
import time
import csv
import matplotlib.pyplot as plt
import pandas as pd
import os

# Initialize Text-to-Speech engine globally
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Choose a voice

# Store API keys securely (use environment variables if possible)
API_KEY = '961e4a4bf91fec24098bc3820c4704fe'
FORECAST_API_KEY = 'c0533613aa33720b516b1ed157a094c8'


def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()


def get_weather(city):
    """Fetches current weather details of a city."""
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] != 200:
            print("Error fetching weather data! Please check the city name.")
            speak("Error fetching weather data! Please check the city name.")
            return None

        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def display_weather(data, city):
    """Displays and speaks out the weather conditions."""
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}\n")

    # Speak weather condition
    if temp >= 27:
        speak(f"It's hot in {city}.")
    elif 23 <= temp < 27:
        speak(f"The weather is normal in {city}.")
    else:
        speak(f"It's cool in {city}.")

    weather_report = f"Weather in {city}: Temperature is {temp} degrees Celsius, Humidity is {humidity} percent, and the condition is {description}."
    speak(weather_report)


def get_forecast(city):
    """Fetches the 5-day forecast (every 3 hours)."""
    base_url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q': city,
        'appid': FORECAST_API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print("Error fetching forecast data!")
            return None

        return response.json()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def display_forecast(forecast_data, city):
    """Displays the 5-day forecast and generates a temperature graph."""
    if not forecast_data:
        return

    print(f"\n5-Day Forecast for {city}:\n")
    forecast_list = [["Time", "Temperature (°C)", "Weather"]]
    times, temperatures = [], []

    for forecast in forecast_data['list']:
        time = forecast['dt_txt']
        temp = forecast['main']['temp']
        weather_desc = forecast['weather'][0]['description']

        print(f"Time: {time}, Temp: {temp}°C, Weather: {weather_desc}")
        forecast_list.append([time, temp, weather_desc])

        # Store for plotting
        times.append(time)
        temperatures.append(temp)

    # Save forecast to CSV
    with open('forecast_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(forecast_list)

    # Get max temperature and announce it
    max_temp = max(temperatures)
    speak(f"The maximum temperature in {city} over the next 5 days is {max_temp} degrees Celsius.")
    print(f"\nMaximum temperature in {city}: {max_temp}°C\n")

    # Plot the data
    plot_forecast(times, temperatures)


def plot_forecast(times, temperatures):
    """Plots a graph of the temperature forecast."""
    plt.figure(figsize=(12, 6))
    plt.plot(times, temperatures, marker='o', color='teal', label='Temperature (°C)')

    plt.title('5-Day Weather Forecast', fontsize=16)
    plt.xlabel('Date & Time', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.xticks(rotation=45, fontsize=8)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    print("\n----- Weather Information -----\n")
    city = input("Enter city name: ")

    # Get current weather
    weather_data = get_weather(city)
    if weather_data:
        display_weather(weather_data, city)

    # Get forecast
    forecast_data = get_forecast(city)
    if forecast_data:
        display_forecast(forecast_data, city)


if __name__ == "__main__":
    main()
