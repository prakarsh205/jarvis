import pyautogui as u
import time
from Head.Mouth import speak
def notepad():
    u.press("win")
    time.sleep(0.5)
    u.write('notepad')
    time.sleep(0.5)
    u.press('enter')
    time.sleep(0.5)
    u.hotkey("ctrl",'o')
    time.sleep(0.5)
    u.write('prakarsh notes')
    time.sleep(0.5)
    u.press('enter')
    time.sleep(0.5)
    u.hotkey('win','h')
    speak('start taking note')


