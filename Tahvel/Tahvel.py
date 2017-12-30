

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

pilt1 = tkinter.PhotoImage(file="pliiats.png")
pilt1 = pilt1.subsample(10,10)

Pnupp = tkinter.Button(frame1, image=pilt1, width=45, height=35, command = pliiats)
Pnupp.image = pilt1
Pnupp.pack(anchor='nw', side="left", padx=10)

pLaius = tkinter.Scale(frame1, from_=0, to=100, orient="horizontal", length=150)
pLaius.pack(anchor='nw', side="left")

def kustut():
    global riist
    riist = "k"
    
pilt2 = tkinter.PhotoImage(file="kustu.png")
pilt2 = pilt2.subsample(10,10)

Knupp = tkinter.Button(frame1, image=pilt2, width=45, height=35, command = kustut)
Knupp.image = pilt2
Knupp.pack(anchor='nw', side="left", padx=10)

def getColor():
    global värv
    värv=askcolor()
    
pilt3 = tkinter.PhotoImage(file="värv.png")
pilt3 = pilt3.subsample(4,5)

värvivalik = tkinter.Button(frame1, image=pilt3, width=45, height=35, command = getColor)
värvivalik.image = pilt3
värvivalik.pack(anchor='nw', side="left")

def deleteall():
    tahvel.delete("all")

Breset = tkinter.Button(frame1, text="RESET", width=18, command = deleteall)
Breset.pack(anchor='nw', padx=50)

tahvel = tkinter.Canvas(frame2, width= 2000, height= 2000, background='white')
tahvel.pack(anchor='nw')

b1 = "üleval"
b3 = "üleval"

def joonistamine():
    tahvel.bind("<Motion>", motion)
    tahvel.bind("<Button-1>", b1alla)
    tahvel.bind("<ButtonRelease-1>", b1üles)
    tahvel.bind("<Button-3>", b3alla)
    tahvel.bind("<ButtonRelease-3>", b3üles)
                
def b1alla(event):
    global b1
    b1 = "all"

def b1üles(event):
    global b1
    b1 = "üleval"
    
def b3alla(event):
    global b3
    b3 = "all"
    
def b3üles(event):
    global b3
    b3 = "üleval"
    
def motion(event):
    global b1, b3
    if b1 == "all":
        global riist, värv
        if riist == "p":
            event.widget.create_polygon(event.x, event.y, event.x+1, event.y+1, outline=värv[1], width=pLaius.get())
        if riist == "k":
            event.widget.create_polygon(event.x, event.y, event.x+1, event.y+1, outline="white", width=pLaius.get())
    if b3 == "all":
        event.widget.create_polygon(event.x, event.y, event.x+1, event.y+1, outline="white", width=pLaius.get())
        
joonistamine()
window.mainloop()