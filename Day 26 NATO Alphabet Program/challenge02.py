weather_celsius = {"Sunday":45, "Monday":24, "Tuesday":12, "Wednesday":36, "Thursday":17, "Friday":27, "Saturday":41}
print(weather_celsius)

weather_farhenheit = {day:(9*celsius)/5+32 for (day,celsius) in weather_celsius.items()}
print(weather_farhenheit)