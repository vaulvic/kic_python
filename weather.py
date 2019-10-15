
import pyowm
from newsapi import NewsApiClient
owm = pyowm.OWM('d45028b6f86ba925fb1e5b0795fe7a3a')
observation = owm.weather_at_place('Krasnoyarsk')
w = observation.get_weather()
d=w.get_temperature('celsius')
c=w.get_wind()
w.get_humidity()
print("Температура:"+str(d['temp'])+"С")
print("Скорость ветра:"+str(c['speed'])+"м/с")
print("Влажность:"+str(w.get_humidity())+"%")
