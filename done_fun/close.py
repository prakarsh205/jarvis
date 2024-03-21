
import random
import time

import pyautogui as ui
from Head.Mouth import speak
from Data.dlg_data.dlg import *

closedlg_random = random.choice(closedlg)
def close():
    speak(closedlg_random)
    ui.press('enter')
    time.sleep(0.5)
    ui.hotkey("alt","f4")
    ui.press('enter')
