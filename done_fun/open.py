import random
import pyautogui as ux
import time
from Head.Mouth import speak
from Data.dlg_data.dlg import *
import webbrowser
import difflib

def openn(text):

    text=text.replace('open','')
    text=text.strip()

    ux.press('win')
    time.sleep(0.5)
    ux.write(text)
    time.sleep(0.5)
    ux.press('enter')

def openweb(text):


    website_name_lower = text.lower()


    if website_name_lower in websites:
        url = websites[website_name_lower]
        webbrowser.open_new_tab(url)
        randonsuccess = random.choice(success_open)
        speak(randonsuccess)
    else:
        matches = difflib.get_close_matches(website_name_lower, websites.keys(), n=1, cutoff=0.6)
        if matches:
            closest_match = matches[0]
            url = websites[closest_match]
            webbrowser.open(url)
            randonsuccess = random.choice(success_open)
            speak(randonsuccess)
        else:
            randonsorry = random.choice(sorry_open)
            speak(randonsorry +" named " + text)

def open(text):
    if "website" in text or "site" in text:
        text = text.replace("open","")
        text = text.replace("site","")
        text = text.strip()
        openweb(text)
    elif "app" in text or "application" in text:
        text = text.replace("app", "")
        text = text.replace("application", "")
        text = text.replace("open", "")
        text = text.strip()
        openn(text)
    else:
        text = text.replace("open", "")
        text = text.strip()
        openn(text)


