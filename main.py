from done_fun.ip_adress import ipa
import threading
from done_fun.loction import loction
# from done_fun.search_google import search_google
from Traning_Model.model import mind
from Traning_Model.model2 import get_response
from done_fun.wish import wish
from done_fun.welcome import welcome
from done_fun.open import open
from done_fun.close import close
from Head.Ear import listen
import pyautogui as gui
from Function.bettry import *
from Function.search_wiki import *
from Function.Youtube import *
from playsound import playsound
from done_fun.check_online_ofline import *
from Function.speed_test import *
from done_fun.clock import *
from Data.dlg_data.dlg import *
from done_fun.take_notes import notepad
from done_fun.todolis import todo
from done_fun.temp import Temp

def cmd():
    wish()

    while True:
        text = listen().lower()
        if text in wake_key_word:
            welcome()
        elif text in bye_key_word:
            res_random = random.choice(res_bye)
            speak(res_random)
            break
        elif text.startswith(("jarvis", "buddy", "jar")):
            text = text.replace("jarvis", "")
            text = text.replace("vis", "")
            text = text.replace("buddy", "")
            text = text.replace("jar", "")
            text = text.strip()
            mind(text)
        elif text.startswith('loction'):
            loction()
        elif text.endswith(("jarvis", "buddy", "jar", " jarvis", " buddy", " jar")):
            text = text.replace("jarvis", "")
            text = text.replace("vis", "")
            text = text.replace("buddy", "")
            text = text.replace("jar", "")
            text = text.strip()
            mind(text)

        elif "jarvis" in text or "jar" in text or "jarvis " in text:
            response = get_response(text)
            speak(response)

        elif "search in google" in text or "search on google" in text:
            text = text.replace("search in google", "")
            text = text.replace("search on google", "")
            text = text.strip()
            search_google(text)

        elif text.endswith(("search in google", "search on google")):
            text = text.replace("search in google", "")
            text = text.replace("search on google", "")
            text = text.strip()
            search_google(text)

        elif "search in youtube" in text or "search on youtube" in text:
            text = text.replace("search in youtube", "")
            text = text.replace("search on youtube", "")
            text = text.strip()
            youtube_search(text)

        elif text.endswith(("search in youtube", "search on youtube")):
            text = text.replace("search in youtube", "")
            text = text.replace("search on youtube", "")
            text = text.strip()
            youtube_search(text)

        elif text.startswith(('how','how to',"who is", "what is", "what was", "who was")):
           print('according to wikipidea', wiki_search(text))

        elif "play music on youtube" in text:
            a = random.choice(q)
            speak(a)
            text = listen().lower()
            play_music_on_youtube(text)

        elif text.startswith(("open", "kholo", "show me")):
            text = text.replace("kholo", "")
            text = text.replace("show me", "")
            text = text.strip()
            open(text)

        elif text in open_input:
            text = text.replace("big", "")
            text = text.replace("khologe", "")
            text = text.replace("kholo", "")
            text = text.strip()
            open(text)

        elif text in close_input:
            close()

        elif "waqt kya hai" in text or "samay kya hai" in text or "kitne baje hain" in text or "kitna samay hua" in text or "tell the time" in text or "time" in text:
              what_is_the_time()

        elif (
            "check battery persent" in text
            or "battery" in text
            or "check battery persentage" in text
        ):
            battey_persentage()

        elif (
            "minimise" in text
            or "minimise the window" in text
            or "minimize karoge" in text
            or "minimize karo" in text
        ):
            speak("minimizing..")
            gui.hotkey("win", "down")
            gui.hotkey("win", "down")

        elif "write" in text or "likho" in text or "right" in text:
            speak("writing")
            text = text.replace("write", "").replace("likho", "").replace("right", "")
            gui.write(text)

        elif "enter" in text or "press enter" in text or "send" in text:
            gui.press("enter")

        elif "select all" in text or "select all paragraph" in text:
            gui.hotkey("ctrl", "a")

        elif "copy" in text or "copy this" in text:
            gui.hotkey("ctrl", "c")

        elif "paste" in text or "paste here" in text:
            gui.hotkey("ctrl", "v")

        elif "undo" in text or "undo karo" in text:
            gui.hotkey("ctrl", "z")

        elif "copy last paragraph" in text:
            gui.hotkey("ctrl", "shift", "c")

        elif (
            "increase volume" in text
            or "volume badhao" in text
            or "increase the volume" in text
        ):
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            print("Volume increased.")
        elif (
            "decrease volume" in text
            or "volume kam karo" in text
            or "decrease the volume" in text
        ):
            gui.press("volumedown")
            gui.press("volumedown")
            gui.press("volumedown")
            gui.press("volumedown")
            gui.press("volumedown")
            speak("Volume decreased.")
            print("Volume decreased.")

        elif "full volume" in text or "full volume kr do" in text:
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            speak("now your system in full volume")
            print("now your system in full volume")

        elif "mute" in text:
            gui.press("volumemute")
            print("Volume muted.")


        elif "visit" in text:
            Nameofweb = text.replace("visit ", "")
            speak(f"visiting {Nameofweb}")
            Link = f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)

        elif "launch" in text:
            Nameofweb = text.replace("launch ", "")
            speak(f"launching {Nameofweb}")
            Link = f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)

        elif "play" in text or "pause" in text or "stop" in text:
            gui.hotkey("space")

        elif text.startswith("search"):
            gui.hotkey("/")
            text = text.replace("search", "")
            gui.hotkey("ctrl", "a")
            time.sleep(0.5)
            gui.press("backspace")
            time.sleep(0.5)
            gui.write(text)
            speak(f"searching {text}")
            print(f"searching {text}")
            time.sleep(1)
            gui.press("enter")

        elif "go back" in text or "back" in text:
            speak("Going Back.")
            gui.hotkey("alt", "left")


        elif "go forward" in text or "forward" in text:
            speak("Going Forward.")
            gui.hotkey("alt", "right")


        elif "stop loading" in text or "stop" in text:
            speak("Stopping Page Load.")
            gui.hotkey("esc")



        elif "scroll up" in text or "scroll page up" in text:
            speak("Scrolling Up.")
            gui.scroll(3)


        elif "scroll down" in text or "scroll page down" in text:
            speak("Scrolling Down.")
            gui.scroll(-3)

        elif "scroll to top" in text:
            speak("Scrolling to Top.")
            gui.press("home")

        elif "scroll to bottom" in text:
            speak("Scrolling to Bottom.")
            gui.press("end")

        elif "open new tab" in text or "new tab" in text:
            speak("Opening New Tab.")
            gui.hotkey("ctrl", "t")

        elif "reopen closed tab" in text or "restore closed tab" in text:
            speak("Reopening Closed Tab.")
            gui.hotkey("ctrl", "shift", "t")


        elif (
            "maximize window" in text or "maximize the window" in text or "maxi" in text
        ):
            speak("Maximizing Window.")
            gui.hotkey("win", "up")

        elif "restore window" in text:
            speak("Restoring Window.")
            gui.hotkey("win", "shift", "up")

        elif "switch window" in text or "next window" in text:
            speak("Switching to Next Window.")
            gui.hotkey("alt", "tab")

        elif "previous window" in text or "back window" in text:
            speak("Switching to Previous Window.")
            gui.hotkey("alt", "shift", "tab")


        elif "open incognito" in text or "private window" in text:
            speak("Opening Incognito Window.")
            gui.hotkey("ctrl", "shift", "n")
        elif "bookmark page" in text or "save page" in text:
            speak("Bookmarking Page.")
            gui.hotkey("ctrl", "d")

        elif "history" in text or "browse history" in text:
            speak("Opening Browsing History.")
            gui.hotkey("ctrl", "h")

        elif "downloads" in text or "download history" in text:
            speak("Opening Downloads History.")
            gui.hotkey("ctrl", "j")

        elif "inspect element" in text or "open developer tools" in text:
            speak("Opening Developer Tools.")
            gui.hotkey("ctrl", "shift", "i")


        elif "clear cookies" in text or "delete cookies" in text:
            speak("Clearing Cookies.")
            gui.hotkey("ctrl", "shift", "del")


        elif "fullscreen" in text or "full screen" in text:
            speak("Entering Fullscreen Mode.")
            gui.hotkey("f11")


        elif "toggle dark mode" in text or "dark theme" in text:
            speak("Toggling Dark Mode.")
            gui.hotkey("ctrl", "shift", "e")


        elif "mute tab" in text:
            speak("Muting Tab.")
            gui.hotkey("ctrl", "m")


        elif "unmute tab" in text:
            speak("Unmuting Tab.")
            gui.hotkey("ctrl", "shift", "m")


        elif "open extensions" in text or "manage extensions" in text:
            speak("Opening Extensions.")
            gui.hotkey("ctrl", "shift", "a")


        elif "browser settings" in text:
            speak("Opening Settings.")
            gui.hotkey("ctrl", ",")


        elif "save page as" in text or "save as" in text:
            speak("Saving Page As.")
            gui.hotkey("ctrl", "s")


        elif "print page" in text or "print" in text:
            speak("Printing Page.")
            gui.hotkey("ctrl", "p")


        elif "clear browsing data" in text or "clear history" in text:
            speak("Clearing Browsing Data.")
            gui.hotkey("ctrl", "shift", "del")

        elif "show desktop" in text or "hide windows" in text:
            speak("Showing Desktop.")
            gui.hotkey("win", "m")
        elif "open notification center" in text or "show notifications" in text:
            speak("Opening Notification Center.")
            gui.hotkey("win", "a")


        elif "show action center" in text or "show action menu" in text:
            speak("Showing Action Center.")
            gui.hotkey("win", "a")


        elif "lock screen" in text :
            speak("Locking Screen.")
            time.sleep(0.5)
            gui.hotkey('win', '8')


        elif "switch user" in text or "change user" in text:
            speak("Switching User.")
            gui.hotkey("win", "l")


        elif "log off" in text or "sign out" in text:
            speak("Logging Off.")
            gui.hotkey("ctrl", "alt", "del")


        elif "shutdown" in text or "turn off computer" in text:
            speak("Shutting Down.")
            gui.hotkey("win", "d")
            time.sleep(0.5)
            gui.hotkey("alt", "f4")

            time.sleep(0.5)
            gui.press("enter")


        elif "restart" in text or "reboot" in text:
            speak("Restarting.")
            gui.hotkey("win", "d")
            time.sleep(0.5)
            gui.hotkey("alt", "f4")
            time.sleep(0.5)
            gui.press("down")
            time.sleep(0.5)
            gui.press("enter")


        elif "sleep" in text or "put computer to sleep" in text:
            speak("Putting Computer to Sleep.")
            gui.hotkey("win", "d")
            time.sleep(0.5)
            gui.hotkey("alt", "f4")
            time.sleep(0.5)
            gui.press("up")
            time.sleep(0.5)
            gui.press("enter")



        elif "zoom in " in text or "current page me zoom in karo" in text:
            speak("Zooming in on the current page.")
            gui.hotkey("ctrl", "+")

        elif text.startswith(
            ("open notepad", "take note", "note", "notepad", "take a note")
        ):
            speak("ok wait a second")
            notepad()
        elif text.startswith(
            (
                "add a task",
                "add task",
                "to do list",
                "add todo",
                "todo",
                "note task",
                "add tas",
                "add a tas",
            )
        ):
            speak("wait a second")
            todo()


        elif "zoom out " in text or "current page me zoom out karo" in text:
            speak("Zooming out on the current page.")
            gui.hotkey("ctrl", "-")


        elif "reset the zoom level" in text or "zoom reset karo" in text:
            speak("Resetting the zoom level to default.")
            gui.hotkey("ctrl", "0")


        elif 'unlock computer' in text:
            speak('unlocking')
            gui.press('enter')
            time.sleep(1)
            gui.press('0')
            time.sleep(0.5)
            gui.press('p')
            time.press(0.5)
            gui.press('l')
            time.press(0.5)
            gui.press('m')
            gui.press('enter')

        elif text in qa_dict:
            ans = qa_dict[text]
            speak_thread = threading.Thread(target=speak, args=(ans,))
            speak_thread.start()
            speak_thread.join()

        elif " check internet speed" in text or "check internet speed" in text:
            check_internet_speed()

        elif "find my ip" in text or "check my ip address" in text or "ip address" in text:
            x = ipa()
            speak(f"sir,your current ip is {x}")


        elif "check temperature" in text or "check temperature outside" in text or "temperature" in text :
            Temp()

        elif 'add file' in text :
            gui.hotkey('shift','n')
            speak('addign new file')
        elif 'where we are'in text:
            loction()

        else:
            pass


def jarv():
    t1=threading.Thread(target=cmd)
    t2=threading.Thread(target=check_plugin_status1)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
jarv()
playsound(r"C:\Users\HP\OneDrive\Desktop\jarvis without any misstakes\mixkit-high-tech-bleep-confirmation-2520.wav")


























































