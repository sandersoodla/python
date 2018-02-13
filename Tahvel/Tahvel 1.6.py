
import tkinter
from tkinter.colorchooser import *

window = tkinter.Tk()
window.title("Tahvel")
window.geometry("1400x900+100+50")
window.configure(background='grey')

riist = "p"
värv = ((0.1, 0.1, 0.1), '#000000')
#kursor = "pencil"

frame1 = tkinter.Frame(width=200, height=100, bg='lightblue')
frame1.pack(anchor='nw', fill='x')

frame2 = tkinter.Frame(width=2000, height=2000)
frame2.pack(side="bottom")


def pliiats():
    global riist, kursor
    riist = "p"
    kursor = "pliiats"
    
pilt1 = tkinter.PhotoImage(file="pliiats.png")
pilt1 = pilt1.subsample(10,10)

Pnupp = tkinter.Button(frame1, image=pilt1, width=45, height=35, command = pliiats)
Pnupp.image = pilt1
Pnupp.pack(anchor='nw', side="left", padx=10)


pLaius = tkinter.Scale(frame1, from_=0, to=200, orient="horizontal", length=300)
pLaius.pack(anchor='nw', side="left")


def kustut():
    global riist, kursor
    riist = "k"
    kursor = "dot"
    
pilt2 = tkinter.PhotoImage(file="kustu.png")
pilt2 = pilt2.subsample(10,10)

Knupp = tkinter.Button(frame1, image=pilt2, width=45, height=35, command = kustut)
Knupp.image = pilt2
Knupp.pack(anchor='nw', side="left", padx=10)


def getColor():
    global värv
    värv=askcolor()
    #if värv = (None, None):
        
    
pilt3 = tkinter.PhotoImage(file="värv.png")
pilt3 = pilt3.subsample(4,5)

värvivalik = tkinter.Button(frame1, image=pilt3, width=45, height=35, command = getColor)
värvivalik.image = pilt3
värvivalik.pack(anchor='nw', side="left")


def ristkülik():
    global riist, xvana, yvana, xuus, yuus
    riist = "ristkülik"
    xvana, yvana, xuus, yuus = None, None, None, None

pilt4 = tkinter.PhotoImage(file="ristkülik.png")
pilt4 = pilt4.subsample(4,4)

ristkülikNupp = tkinter.Button(frame1, image=pilt4, width=45, height=35, command=ristkülik)
ristkülikNupp.image = pilt4
ristkülikNupp.pack(anchor='nw', side="left", padx=(50,5))


def ring():
    global riist, xvana, yvana, xuus, yuus
    riist = "ring"
    xvana, yvana, xuus, yuus = None, None, None, None

pilt5 = tkinter.PhotoImage(file="ring.png")
pilt5 = pilt5.subsample(14,14)

ringNupp = tkinter.Button(frame1, image=pilt5, width=45, height=35, command=ring)
ringNupp.image = pilt5
ringNupp.pack(anchor='nw', side="left", padx=(5,50))


tekstKast = tkinter.Entry(frame1, width=25)
tekstKast.pack(anchor='nw', padx=(5,5))

def tekst():
    global riist, tjekst
    riist = "t"
    tjekst = tekstKast.get()

tekstNupp = tkinter.Button(frame1, width=20, height=1, text="ENTER", command=tekst)
tekstNupp.pack(anchor='nw', side="left", padx=(5,5))


def deleteall():
    global xvana, yvana, xuus, yuus
    tahvel.delete("all")
    xvana = None
    yvana = None
    xuus = None
    yuus = None

Breset = tkinter.Button(frame1, text="RESET", width=18, command = deleteall)
Breset.pack(anchor='nw', padx=50)

tahvel = tkinter.Canvas(frame2, width= 2000, height= 2000, background='white')
tahvel.pack(anchor='nw')
#tahvel.config(cursor=kursor)

b1 = "üleval"
b3 = "üleval"
xvana, yvana = None, None
xuus, yuus = None, None


def hiirInput():
    tahvel.bind("<Motion>", joonistamine)
    tahvel.bind("<Button-1>", b1alla)
    tahvel.bind("<ButtonRelease-1>", b1üles)
    tahvel.bind("<Button-3>", b3alla)
    tahvel.bind("<ButtonRelease-3>", b3üles)
    
def b1alla(event):
    global b1, xvana, yvana
    b1 = "all"
    if riist == "ristkülik" or riist == "ring":
        print(event.x, event.y)
        xvana = event.x
        yvana = event.y

def b1üles(event):
    global b1, xuus, yuus
    b1 = "üleval"
    if riist == "ristkülik" or riist == "ring":
        print(event.x, event.y)
        xuus = event.x
        yuus = event.y
    
def b3alla(event):
    global b3
    b3 = "all"
    
def b3üles(event):
    global b3
    b3 = "üleval"
    
def joonistamine(event):
    global b1, b3
    if b1 == "all":
        global riist, värv, xvana, yvana, tjekst
        if riist == "p":
            event.widget.create_polygon(event.x, event.y, event.x+1, event.y+1, outline=värv[1], width=pLaius.get())
        if riist == "k":
            event.widget.create_polygon(event.x, event.y, event.x+1, event.y+1, outline="white", width=pLaius.get())
        if riist == "t":
            event.widget.create_text(event.x, event.y, fill=värv[1], text=tjekst, font=("Helvetica", pLaius.get()))
    if b1 == "üleval":
        if riist == "ristkülik" and xvana != None and yvana != None and xuus != None and yuus != None:
            event.widget.create_rectangle(xvana, yvana, xuus, yuus, outline=värv[1], width=5)
        if riist == "ring" and xvana != None and yvana != None and xuus != None and yuus != None:
            event.widget.create_oval(xvana, yvana, xuus, yuus, outline=värv[1], width=5)
    if b3 == "all":
        event.widget.create_polygon(event.x, event.y, event.x+1, event.y+1, outline="white", width=pLaius.get())
        
hiirInput()
window.mainloop()