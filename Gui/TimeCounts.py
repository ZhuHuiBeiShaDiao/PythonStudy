# coding:utf-8
import time
from tkinter import *
import threading

info = {
    'total_time':60
}

def make_app():
    _font = ['Hack',25,'bold']
    app = Tk()
    Label(name='lb',text=0,font=_font).pack()
    Button(name='btn',text='开始',command=time_counts).pack()
    Entry(name='ipt').pack()
    app.geometry('150x100')
    return app

def time_counts():
    def _counts():
        while info['total_time']:
            info['total_time'] -= 1
            print(info['total_time'])
            time.sleep(1)

    t = threading.Thread(target=_counts,name='timer')
    t.start()
# 通过修改total_time的值，来完成停止操作
def time_stop():
    info['total_time'] = 0

def ui_watcher():
    # 将input框禁用的函数
    def _update_input():
        ipt = app.children['ipt']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        ipt['state'] = 'disabled' if timer else 'normal'
    # 修改按钮状态的函数
    def _update_button():
        btn = app.children['btn']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        btn['text'] = '停止' if timer else '开始'
        btn['command'] = time_stop if timer else time_counts

    def _get_time():
        ipt = app.children['ipt']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if not timer and ipt.get():
            info['total_time'] = int(ipt.get())

    def _update_time():
        lb = app.children['lb']
        lb['text'] = info['total_time']

    def _main():
        while True:
            print(threading.enumerate())
            _get_time()
            _update_time()
            _update_button()
            _update_input()
            time.sleep(0.5)

    t = threading.Thread(target=_main,name='watcher')
    t.start()

app = make_app()
app.after(0,ui_watcher)
app.mainloop()