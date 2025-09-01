import mouse
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import keyboard
import threading
import random

is_on = False
myhotkey = "f6"


def get_boxes():
    hotbarslots = []
    for i, v in enumerate(hotbar):
        if v.get():
            hotbarslots.append(i+1)
    return(hotbarslots)


def scroll(): # actually do the scrolling
    # global is_on
    global uhotbar
    while is_on:
        if uhotbar.get():
            slots = get_boxes()
            total = len(slots)
            rand = random.randint(0, total-1)
            while is_on:
                previous = rand
                rand = random.randint(0, total-1)
                if rand == previous:
                    continue

                keyboard.press(slots[rand])
                keyboard.release(slots[rand])
                time.sleep(0.02)

        else:
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
        return

    else:
        myhotkey = rkey
        keyboard.remove_hotkey(str(oldkey))
        keyboard.add_hotkey(rkey, toggle)
        hotkeybut.config(text=rkey)

keyboard.add_hotkey(myhotkey, toggle)

root = Tk()

hotbar = []

root.minsize(200, 100)
root.title("Scrollie")
frm = ttk.Frame(root, padding=10)
frm.grid()

indicator = ttk.Label(frm, text="off", foreground="red", font=("comic sans", 25))
indicator.grid(column=0, row=0)
ttk.Label(frm,  text="button to change hotkey\n(esc to cancel)").grid(column=0, row=1)

hotkeybut = ttk.Button(frm, text="f6", command=set_hotkey)
hotkeybut.grid(column=0, row=2)

uhotbar = tk.BooleanVar()
usehotbar = tk.Checkbutton(frm, text="Use hotbar slots instead of scrollwheel", variable=uhotbar)
usehotbar.grid(column=0, row=3)

hotbarcontainer = tk.Frame(frm)
hotbarcontainer.grid(column=0, row=4, sticky="n")
for i in range(9):
    v = tk.BooleanVar()
    hotbar.append(v)
    cb = tk.Checkbutton(hotbarcontainer, text=f"{i+1}", variable=v)
    cb.grid(column=i, row=0, padx=5)


ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)


root.wm_attributes("-topmost", True)
root.mainloop()
