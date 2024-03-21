import pyautogui as u
import time


def sutdown():
    u.hotkey("win", "d")
    time.sleep(0.5)
    u.hotkey("alt", "f4")
    time.sleep(0.5)
    u.press("enter")
