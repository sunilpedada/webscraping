from urllib.request import urlopen
import json
def temp():
    ip=input("enter city")
    x=urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ip+",india&APPID=107556c8a65b7ef5d7137fcf27df1f8f")
    y=json.load(x)
    print(y)
    print(y["main"])
    t=y["main"]
    temperature=t['temp']
    conv=temperature-273.14
    print(conv)
temp()