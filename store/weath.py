import pyowm as pyowm

owm = pyowm.OWM('0b21223934144e3b696bb4311b03e797')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('City, State')
w = observation.weather
temp = w.temperature('celsius')
status = w.detailed_status
print("It is currently " + str(int(temp['temp'])) + " degrees and " + status)
print(temp)
##########################


cities = ["tokyo", "jakarta"]

for city in cities:
    city_weather = owm.weather_at_place(city)
    weather = city_weather.get_weather()
    print(weather.get_pressure()['press'])