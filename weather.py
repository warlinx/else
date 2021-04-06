from pyowm.utils import timestamps

appid = "0b21223934144e3b696bb4311b03e797"


from pyowm import OWM

from pyowm.utils import timestamps

owm = OWM(appid)  # You MUST provide a valid API key

# Search for current weather in London (Great Britain)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('London,GB')
forecast = mgr.forecast_at_place('London,GB', 'dayly')

w = observation.weather

pr = w.pressure['press']
print(pr)
print(forecast)


