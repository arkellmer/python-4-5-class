#andrew kellmer 9/25/18

from tkinter import*
from tkinter import ttk
from tkinter import font
import winsound
import time
import calendar
import datetime
    
def current_time():

    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds % 60
    minutes = seconds // 60
    current_minutes = minutes % 60
    hours = minutes // 60
    current_hour = hours % 24

    current_hour = current_hour - 6

    if current_hour >= 12:
        tag = "PM"

    else:
        tag = "AM"

    a = str(14)+":"+str(0)+":"+str(59)+tag

    timex = str(current_hour)+":"+ str(current_minutes)+":"+ str(current_seconds)+tag
    if timex == a:
        beep()
    return timex

def beep():
    winsound.Beep(540,8000)

x = current_time()
#print(x)

def quit(*args):
    root.destroy()

def show_time():
    time = current_time()
    txt.set(time)
    root.after(1000, show_time)

root = Tk()
root.attributes("-fullscreen",True)
root.configure(background="Green")
root.bind("x",quit)
root.after(1000, show_time)
fnt = font.Font(family = 'Helvetica', size = 60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = "Yellow", background = "Green")
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()

root.bind(" ",beep)



    
