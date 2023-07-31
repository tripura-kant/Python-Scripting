##
import json

import requests

city = input("Enter your city \n")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c4b1bc888916b8e991b78d5f81fcf818"

r = requests.get(url)
print(r.text)
dic = json.loads(r.text)
