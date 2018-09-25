from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import time
import calendar
import datetime

h=input("Hour: ")
m=input("Min: ")
s=input("Sec: ")

def clock(h,m,s):
    totalMilliseconds = calendar.timegm(time.gmtime())
    totalMilliseconds = totalMilliseconds *1000
    totalSeconds = totalMilliseconds / 1000
    currentSecond = int(totalSeconds % 60)

    totalMinutes = totalSeconds / 60
    currentMinute = int(totalMinutes % 60)

    totalHours = totalMinutes / 60
    currentHour = int(totalHours % 24)
    #timezone
    currentHour -= 6
    
    if currentHour >=12:
        tag="PM"
        currentHour -= 12
    else:
        tag="AM"
        
    a = str(h)+":"+str(m)+":"+str(s)+tag
    #format
    timex = str(currentHour)+":"+ str(currentMinute)+":"+str(currentSecond)+tag
    if timex == a:
        beep()
    return timex

def beep():
    winsound.Beep(600,400)
    winsound.Beep(700,400)
    winsound.Beep(740,400)
    winsound.Beep(700,400)
    winsound.Beep(600,400)
    winsound.Beep(700,400)
    winsound.Beep(740,400)
    winsound.Beep(700,400)

    winsound.Beep(400,500)
    winsound.Beep(500,500)
    winsound.Beep(540,500)
    winsound.Beep(500,500)
    winsound.Beep(400,500)
    winsound.Beep(500,500)
    winsound.Beep(540,500)
    winsound.Beep(500,500)


x=clock(h,m,s)
print(x)

def quit(*args):
    root.destroy()
def show_time():
    time = clock(h,m,s)
    txt.set(time)
    root.after(1000, show_time)



root = Tk()
root.attributes("-fullscreen",True)
bckclr = input("Background color: ")
txtclr = input("Text Color: ")
root.configure(background=bckclr)
root.bind("x",quit)
root.after(1000, show_time)
fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground=txtclr,background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()












