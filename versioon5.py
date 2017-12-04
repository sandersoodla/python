import tkinter
from tkinter.colorchooser import *

window = tkinter.Tk()
window.title("Tahvel")
window.geometry("1000x600")
window.configure(background='grey')

riist = "p"

def pliiats():
    global riist
    riist = "p"

Pnupp = tkinter.Button(window, text="Pliiats", width=18, command = pliiats)
Pnupp.pack(anchor='w')

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
        global xvana, yvana, riist, värv
        if xvana != None and yvana != None and riist == "p":
            event.widget.create_line(xvana, yvana, event.x, event.y, smooth=True, fill=värv[1])
        if xvana != None and yvana != None and riist == "k":
            event.widget.create_line(xvana, yvana, event.x, event.y, smooth=True, fill='white', width=20)
        xvana = event.x
        yvana = event.y

joonistamine()
window.mainloop()