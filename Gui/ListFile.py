from tkinter import *
import os

app = Tk()
app.geometry('300x400')
label = Label(text='All files',font=('Arial',25,'bold'))
label.pack()
listbox = Listbox(bg='#f2f2f2',fg='red')
listbox.pack(fill=BOTH,expand=True)
path = './'
files = os.listdir(path)
for f in files:
    listbox.insert(END, f)

app.mainloop()