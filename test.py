import tkinter

window = tkinter.Tk()
window.title("OK")
window.geometry("1000x600")
window.configure(background='white')

entUser = tkinter.Entry(window)
entUser.pack(anchor='w')

entPass = tkinter. Entry(window)
entPass.pack(anchor='w')

Pnupp = tkinter.Button(window, text="Pliiats", width=18)
Pnupp.pack(anchor='w')

Knupp = tkinter.Button(window, text="Kustutuskumm", width=18)
Knupp.pack(anchor='w')

window.mainloop()