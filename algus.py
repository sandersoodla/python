#joonistusprogrammi aken
import tkinter

window = tkinter.Tk()
window.title("OK")
window.geometry("400x400")
window.configure(background='grey')

entUser = tkinter.Entry(window)
entUser.pack()

entPass = tkinter. Entry(window)
entPass.pack()

btnEnter = tkinter.Button(window, text="Start")
btnEnter.pack()

window.mainloop()