import requests
from Head.Mouth import speak

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()

    return speak(res["joke"])

get_random_joke()
