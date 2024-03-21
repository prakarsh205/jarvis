import pyautogui as u
import time
def todo():
    u.press('win')
    time.sleep(0.5)
    u.write('todo')
    time.sleep(0.5)
    u.press('enter')
    time.sleep(2)
    u.hotkey('ctrl','n')
    time.sleep(0.8)
    u.hotkey('win','h')

