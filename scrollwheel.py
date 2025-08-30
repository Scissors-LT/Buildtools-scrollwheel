import mouse
from tkinter import *
from tkinter import ttk
import time
import keyboard
import threading

is_on = False
myhotkey = "f6"

def scroll(): # actually do the scrolling
    global is_on
    while is_on:
        mouse.wheel(-1)
        time.sleep(0.001)


def toggle():
    global is_on
    if not is_on:
        is_on = True
        indicator.config(text="on", foreground="green", font=("comic sans", 25))
        threading.Thread(target=scroll, daemon=True).start() # start scrolling and set the big label to on
    else:
        is_on = False
        indicator.config(text="off", foreground="red", font=("comic sans", 25)) # stop and set label to off

def set_hotkey():
    global myhotkey
    oldkey = myhotkey
    rkey = keyboard.read_key() # wait for keypress and then continue

    if rkey == 'esc':
        print("stopped")
        return
    else:
        myhotkey = rkey
        keyboard.remove_hotkey(str(oldkey))
        keyboard.add_hotkey(rkey, toggle)
        hotkeybut.config(text=rkey)
        print(rkey)

keyboard.add_hotkey(myhotkey, toggle)

root = Tk()
root.minsize(200, 100)
root.title("scrolling thing")
frm = ttk.Frame(root, padding=10)
frm.grid()
indicator = ttk.Label(frm, text="off", foreground="red", font=("comic sans", 25))
indicator.grid(column=0, row=0)
ttk.Label(frm,  text="button to change hotkey\n(esc to cancel)").grid(column=0, row=1)
hotkeybut = ttk.Button(frm, text="f6", command=set_hotkey)
hotkeybut.grid(column=0, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)
root.wm_attributes("-topmost", True)
root.mainloop()
