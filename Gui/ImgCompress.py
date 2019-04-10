from PIL import Image as Img
from tkinter import *
from tkinter.filedialog import *

files = {
    'path':[]
}

def MakeApp():
    app = Tk()
    Label(app, text='Image compress tool', font=('Arial', 20, 'bold')).pack()
    Listbox(app, name='lbox', bg='#E0FFFF').pack(fill=BOTH, expand=True)
    Button(app, text='open', command=getdata).pack()
    Button(app, text='compress', command=compress).pack()
    app.geometry('300x400')
    return app

def getdata():
    paths = askopenfilenames()
    lbox = app.children['lbox']
    files['path'] = paths

    if files['path']:
        for path in paths:
            lbox.insert(END, path.split('/')[-1])

def compress():
    outpdir = './ImgOutDir/'
    if not os.path.exists(outpdir):  # 检测是否有image目录没有则创建
        os.makedirs(outpdir)

    for path in files['path']:
        name = path.split('/')[-1]
        image = Img.open(path)
        image.save(outpdir + 'c_' + name, quality=60)

app = MakeApp()
app.mainloop()