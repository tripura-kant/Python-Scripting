'''
This program will search for songs on iTunes using the iTunes API.
'''
import sys

import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"] + " - " + result["artistName"])
