from pynput.keyboard import Key,Listener
import os 
keys=[]
def on_press(key):
    global keys
    #keys.append(str(key).replace("'",""))
    string = str(key).replace("'","")
    keys.append(string)
    main_string = "".join(keys)
    print(main_string)
    if "/**/" in main_string:
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        keys = []
    elif "code" in main_string:
        os.startfile("C:\\Users\\abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        keys = []
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()