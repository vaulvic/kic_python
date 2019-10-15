
import pyowm
from newsapi import NewsApiClient
owm = pyowm.OWM('')
observation = owm.weather_at_place('Krasnoyarsk')
w = observation.get_weather()
d=w.get_temperature('celsius')
c=w.get_wind()
w.get_humidity()
print("Температура:"+str(d['temp'])+"С")
print("Скорость ветра:"+str(c['speed'])+"м/с")
print("Влажность:"+str(w.get_humidity())+"%")
