import requests

'''
    Function to fetch weather data
'''


def get_weather(location, api_key):
    # OpenWeatherMap API endpoint
    url = (f"http://api.openweathermap.org/data/2.5/weather?q="
           f"{location}&appid={api_key}&units=metric")

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extract the relevant data
            main = data['main']
            weather = data['weather'][0]

            # Get the temperature, humidity, and weather condition
            temperature = main['temp']
            humidity = main['humidity']
            condition = weather['description']

            # Display the data
            print(f"\nWeather in {location}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {condition.capitalize()}")
        else:
            print(f"Error: {data['message']}. Please check the city name or ZIP code.")
    except Exception as e:
        print(f"Error: Unable to fetch data. {e}")


api_key = "ff1838733022b20741489475e611c020"

# Ask the user for a location (city or ZIP code)
location = input("Enter the city name or ZIP code: ")

# Fetch and display the weather data
get_weather(location, api_key)
