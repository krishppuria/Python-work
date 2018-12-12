import json
import requests
user_input=input("Enter the city name: ")
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+user_input
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url = url1 + url2 + url3
result=requests.get(url)
#print(result.text)
jsondata=result.json()
print("Latitude:  ",jsondata['coord']['lat'])
print("Longitude:  ",jsondata['coord']['lon'])
print("Weather:  ",jsondata['weather'][0]['main'])
print("Wind Speed:  ",jsondata['wind']['speed'])
print("Sun Rise:  ",jsondata['sys']['sunrise'])
print("Sun Set:  ",jsondata['sys']['sunset'])
