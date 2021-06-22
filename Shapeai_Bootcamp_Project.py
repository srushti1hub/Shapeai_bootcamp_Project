import requests
import json
from datetime import datetime
API_Key = '8918cd3f85ebd5f347b6f4eeb7c60b43'
#Input from the user for loaction
location = input('Enter the city : ')
Complete_API_Link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+API_Key
API_Link = requests.get(Complete_API_Link,'allow_redirects=True')
API_Data = API_Link.json()
#Longitude of Location
longitude = API_Data['coord']['lon']
#Latitude of Location
latitude = API_Data['coord']['lat']
#Tempature of Location
temp = ((API_Data['main']['temp']) - 273.15)
#Weather Description of Location
description = API_Data['weather'][0]['description']
#Humidity of Location
humidity = API_Data['main']['humidity']
#Pressure of Location
pressure = API_Data['main']['pressure']
#Wind Speed at Location
wind_speed = API_Data['wind']['speed']
today = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
#Displaying All Information on Console
print("Entered City   : "+location)
print("Longitude      : ",longitude,"\nLatitude       : ",latitude)
print("Temperature    : ",temp, "C")
print("Description    : ",description)
print("Humidity       : ",humidity,"%")
print("Pressure       : ",pressure,"hPa")
print("Wind Speed     : ",wind_speed,"m/s")
#Recording the Information in txt format
#The file will be downloaded in PC
open('Weatherinfo.txt','wb').write(API_Link.content)
