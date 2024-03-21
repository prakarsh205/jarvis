from requests import get
from Head.Mouth import speak

def ipa():
    ipaa=get('https://api.ipify.org').text
    return ipaa


