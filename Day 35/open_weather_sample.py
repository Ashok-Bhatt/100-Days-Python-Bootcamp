import requests
import json

API_KEY = "Enter Your Own API Key"
city = "Vadodara"
latitude = 35.5
longitude = 152.5

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={API_KEY}")
print(response.status_code)

if (response.status_code == 200):

    data = response.json()
    json_data = json.dumps(data, indent=4)

    print(f"Weather id of first forecast: {data['list'][0]['weather'][0]['id']}")

    condition_codes = []
    is_raining = False

    for index, weather in enumerate(data["list"]):
        code = weather["weather"][0]["id"]
        if (index < 4):
            condition_codes.append(code)
        if code < 700:
            is_raining = True
    
    print(condition_codes)
    if is_raining:
        print("Bring Umbrella")

    with open("5_days_forecast.txt", "w") as file:
        file.write(json_data)