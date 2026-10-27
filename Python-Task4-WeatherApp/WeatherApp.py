import requests

with open("api_key.txt") as f:
    API_KEY = f.read().strip()

URL = "https://api.openweathermap.org/data/2.5/weather"

while True:
        
        city = input("Enter the city name:").strip()

        if city == "":
              print("Error: City name cannot be empty. Please enter a valid city name.")
              continue
        
        try:
            response = requests.get(URL, params={"q": city, "appid" : API_KEY,"units" : "metric"}, timeout = 5)

            if response.status_code == 404 :
                  print("City not found")
                  continue
            elif response.status_code == 401 :
                  print("Invalid API key")
                  break
            elif response.status_code != 200 :
                  print("Something went wrong. Please try again.")
                  continue
              
            data = response.json()

            temp_c = data["main"]["temp"]
            temp_f = temp_c * 9 / 5 + 32

            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            wind = data["wind"]["speed"]
            print(f"\nWeather in {city}")
            print(f"Temperature: {temp_c:.1f}C / {temp_f:.1f}F")
            print(f"Humidity : {humidity}%")
            print(f"Condition: {description}")
            print(f"Wind speed: {wind} m/s\n")

        except requests.exceptions.Timeout:
                  print("Request timed out, Try again")     
        except requests.exceptions.RequestException:
                  print("Network error, check your internet connection")

        another_city = input("Do you want to check another city?[y/n]").lower()
        if another_city != "y" :
               break
