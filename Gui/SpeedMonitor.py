import psutil
import time
from tkinter import *

def MakeApp():
    app = Tk()
    app.geometry('300x150')
    app.config(bg='#303030')

    Label(text='SpeedMonitor',
          font=('Arial', '25', 'bold'),
          bg='#303030',
          fg='white'
          ).pack()

    Label(name='lb2',
          text='-',
          font=('Arial', '20', 'bold'),
          bg='#303030',
          fg='white'
          ).pack()

    return app

def getspeed():
    # china
    # psutil.net_io_counters(pernic=True)['en0']
    s1 = psutil.net_io_counters(pernic=True)['以太网']
    time.sleep(1)
    s2 = psutil.net_io_counters(pernic=True)['以太网']

    tick_recv = (s2.bytes_recv - s1.bytes_recv) / 1024
    tick_sent = (s2.bytes_sent - s1.bytes_sent) / 1024

    tick_recv = ('%.2f' % tick_recv)
    tick_sent = ('%.2f' % tick_sent)

    return str(tick_recv) + 'kb/s ' + '/ ' + str(tick_sent) + 'kb/s'


def ui_update(do):
    data = do()
    lb2  = app.children['lb2']
    lb2.config(text=data)
    app.after(1000, lambda : ui_update(do))


app = MakeApp()
app.after(1000, lambda : ui_update(getspeed))
app.mainloop()