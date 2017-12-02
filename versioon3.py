import tkinter

window = tkinter.Tk()
window.title("Tahvel")
window.geometry("1000x600")
window.configure(background='grey')

ent1 = tkinter.Entry(window, width=21)
ent1.pack(anchor='w')

ent2 = tkinter. Entry(window, width=21)
ent2.pack(anchor='w')

Pnupp = tkinter.Button(window, text="Pliiats", width=18)
Pnupp.pack(anchor='w')

Knupp = tkinter.Button(window, text="Kustutuskumm", width=18)
Knupp.pack(anchor='w')

tahvel = tkinter.Canvas(window, width=960, height= 600, background='white')
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
        global xvana, yvana
        if xvana != None and yvana != None:
            event.widget.create_line(xvana, yvana, event.x, event.y, smooth='TRUE')
        
        xvana = event.x
        yvana = event.y

joonistamine()
window.mainloop()