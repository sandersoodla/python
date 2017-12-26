

import tkinter
from tkinter.colorchooser import *

window = tkinter.Tk()
window.title("Tahvel")
window.geometry("1200x800")
window.configure(background='grey')

riist = "p"

def pliiats():
    global riist
    riist = "p"
    
frame1 = tkinter.Frame(width=400, height=100, bg='lightblue')
frame1.pack(anchor='nw', fill='x')

frame2 = tkinter.Frame(width=2000, height=2000)
frame2.pack(side="bottom")

Pnupp = tkinter.Button(frame1, text="Pliiats", width=18, command = pliiats)
Pnupp.pack(anchor='nw', side="left")

pLaius = tkinter.Scale(frame1, from_=0, to=100, orient="horizontal", length=150)
pLaius.pack(anchor='nw', side="left")

def kustut():
    global riist
    riist = "k"

Knupp = tkinter.Button(frame1, text="Kustutuskumm", width=18, command = kustut)
Knupp.pack(anchor='nw', side="left")

def getColor():
    global värv
    värv=askcolor()

värvivalik = tkinter.Button(frame1, text="Vali värv", width=18, command = getColor)
värvivalik.pack(anchor='nw', side="left")

def deleteall():
    tahvel.delete("all")

Breset = tkinter.Button(frame1, text="RESET", width=18, command = deleteall)
Breset.pack(anchor='nw',padx=50)

tahvel = tkinter.Canvas(frame2, width= 2000, height= 2000, background='white')
tahvel.pack(anchor='nw')

b1 = "up"
xvana, yvana = None, None

def joonistamine():
    tahvel.bind("<Motion>", motion)
    tahvel.bind("<Button-1>", b1alla)
    tahvel.bind("<ButtonRelease-1>", b1üles)
                
def b1alla(event):
    global b1
    b1 = "all"

def b1üles(event):
    global b1, xvana, yvana
    b1 = "üleval"
    xvana = None
    yvana = None
    
def motion(event):
    if b1 == "all":
        global riist, värv
        if riist == "p":
            event.widget.create_polygon(event.x, event.y, event.x+1, event.y+1, outline=värv[1], width=pLaius.get())
        if riist == "k":
            event.widget.create_polygon(event.x, event.y, event.x+1, event.y+1, outline="white", width=pLaius.get())
        
joonistamine()
window.mainloop()