from tkinter import *
import tkinter.messagebox
import multiprocessing
import os
from runpy import run_path

    #tkinter.messagebox.showinfo('提示', '人生苦短')
    #tkinter.messagebox.showwarning('警告', '明日有大雨')
    #tkinter.messagebox.showerror('错误', '出错了')
    #tkinter.messagebox.askokcancel('提示', '要执行此操作吗') True False
    #tkinter.messagebox.askquestion('提示', '要执行此操作吗') yes,no
    #tkinter.messagebox.askyesno('提示', '要执行此操作吗') yes,no
    #tkinter.messagebox.askyesnocancel('提示', '要执行此操作吗')True,False,None
    #tkinter.filedialog.askopenfilename() one file
def runpy():
    lbox = app.children['lbox']
    file = lbox.get(ACTIVE)

    for child in multiprocessing.active_children():
        if child.name == file:
            tkinter.messagebox.showerror('error', 'runing')
            print('runing')
            return

    # windows
    p = multiprocessing.Process(name=file, target=run_path, args=(file,))

    # mac/linux
    #p = multiprocessing.Process(name=file, target=lambda  : run_path(file))
    p.start()

def stoppy():
    lbox = app.children['lbox']
    file = lbox.get(ACTIVE)

    r = tkinter.messagebox.askquestion('kill', 'kill All or ' + file)

    for p in multiprocessing.active_children():
        if r == 'yes':
            p.terminate()
        else:
            if p.name == file:
                p.terminate()

def ui_make_lit():
    lbox = app.children['lbox']
    for file in os.listdir():
        lbox.insert(END, file)

def MakeApp():
    app = Tk()
    #app.geometry('300x150')
    app.title('GUI')
    #app.resizable(False, False)
    Listbox(name='lbox').pack()
    Button(text='Run', command=runpy).pack()
    Button(text='Stop', command=stoppy).pack()
    return app

def processMonitor():
    print(multiprocessing.active_children())
    lbox = app.children['lbox']
    file = lbox.get(ACTIVE)
    print(file)
    app.after(1000, processMonitor)

# windows must need if
if __name__ == '__main__':
    app = MakeApp()
    app.after(500, ui_make_lit)
    app.after(1000, processMonitor)
    app.mainloop()
