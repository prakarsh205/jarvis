import psutil
import time
from Head.Mouth import speak
import random
from Data.dlg_data.dlg import *

def battery_alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            random_low = random.choice(low_b)
            speak(random_low)

        elif percent < 10:
            random_low = random.choice(last_low)
            speak(random_low)

        elif percent == 100:
            random_low = random.choice(full_battery)
            speak(random_low)
        else:
            pass

        time.sleep(1500)


def battey_persentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)

    speak(f"the device is running on {percent}% battery power")

previous_state = None
plug_in1 = ["charger is plugged check conform", "battery is charging that means charger is plugged check completed"]
plug_out1 = ["Charger status unplugged", "battery is not charging that means charger is not plugged check completed"]
def check_plugin_status1():
    global previous_state

    battery = psutil.sensors_battery()

    if battery.power_plugged != previous_state:
        if battery.power_plugged:
            random_low = random.choice(plug_in1)
            speak(random_low)
        else:
            random_low = random.choice(plug_out1)
            speak(random_low)
        previous_state = battery.power_plugged

