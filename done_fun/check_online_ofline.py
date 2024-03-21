# check online status
import requests
from Head.Mouth import speak


def is_online(url="http://www.google.com",timeout=5):
    try:
        respone=requests.get(url,timeout=timeout)
        return respone.status_code>=200 and respone.status_code<300
    except requests.ConnectionError:
        return False
def inter():
    if is_online():
        return "hey online"
    else:
        return "ofline"
pre=None
def onl():
    while True:
        try:
            curet=inter()
            if curet!=pre:
                speak(curet)
                pre=curet
        except Exception as e:
            pass
