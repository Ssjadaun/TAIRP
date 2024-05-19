from tkinter import *
from time import *
def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    time_label.after(1000,update)

window = Tk()

time_label = Label(window,font=('Arial',50),fg="#00FF00",bg="black")
time_label.pack()

update()

window.mainloop()

