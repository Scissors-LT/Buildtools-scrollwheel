import mouse
from tkinter import *
from tkinter import ttk
import time
import keyboard
import threading

is_on = False

def scroll():
    global is_on
    while is_on:
        mouse.wheel(-1)
        time.sleep(0.001)


def toggle():
    global is_on
    if not is_on:
        is_on = True
        threading.Thread(target=scroll, daemon=True).start()
        print("started")
    else:
        is_on = False
        print("stopped")

keyboard.add_hotkey("f6", toggle)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm,  text="Press F6 to start/stop").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()
