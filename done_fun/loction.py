import requests
from requests import get
from Head.Mouth import speak
import json
def loction():
    try:
        ipa= requests.get('https://get.geojs.io/v1/ip/geo/49.34.84.64.json')
        data=json.loads(ipa.text)

        speak(f"we are in state {data['region']} of {data['country']} contry")

    except Exception as e:
        print(e)
