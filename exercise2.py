weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
weather_ff = {day:temp * (9/5) + 32 for (day, temp) in weather_c.items()}

# new_dict {new_key:new value  for (key, value) in dict.items()}
#(temp_c * 9/5) + 32 = temp_f

print(weather_f)
print(weather_ff)
