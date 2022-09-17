from tkinter import *
from tkinter.ttk import *
from time import strftime
import time

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('ds-digital', 50, 'bold'),
            background='white',
            foreground='blue')

lbl.pack(anchor='center')
time()
mainloop()
