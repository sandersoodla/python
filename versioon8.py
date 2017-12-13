

import tkinter
from tkinter.colorchooser import *

window = tkinter.Tk()
window.title("Tahvel")
window.geometry("1000x600")
window.configure(background='grey')

riist = "p"
objectlist = []

def pliiats():
    global riist
    riist = "p"

Pnupp = tkinter.Button(window, text="Pliiats", width=18, command = pliiats)
Pnupp.pack(anchor='w')

pLaius = tkinter.Scale(window, from_=0, to=100, orient="horizontal", length=150)
pLaius.pack(anchor='nw')

def kustut():
    global riist
    riist = "k"

Knupp = tkinter.Button(window, text="Kustutuskumm", width=18, command = kustut)
Knupp.pack(anchor='w')

def getColor():
    global värv
    värv=askcolor()

värvivalik = tkinter.Button(text="Vali värv", width=18, command = getColor)
värvivalik.pack(anchor='nw')

def deleteall():
    tahvel.delete("all")

Breset = tkinter.Button(window, text="RESET", width=18, command = deleteall)
Breset.pack()

tahvel = tkinter.Canvas(window, width= 2000, height= 2000, background='white')
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
            objectlist.append(event.widget.create_polygon(event.x, event.y, event.x+1, event.y+1, outline=värv[1], width=pLaius.get()))
            print(len(objectlist))
        if riist == "k":
            event.widget.delete(event.x, event.y, event.x+1, event.y+1)
        
joonistamine()
window.mainloop()