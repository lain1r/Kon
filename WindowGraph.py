import tkinter as tk
import numpy as np

from python.WindowCom import SerialPlotter

PORT = "COM3"
BAUDRATE = 9600
MAXLEN = 200

root = tk.Tk()

frmDivTitle = tk.Frame(root)
frmDivTitle.pack(side = tk.TOP, fill = tk.BOTH)

frmTitle = tk.Frame(master=frmDivTitle)
frmTitle.pack(side= tk.LEFT, fill = tk.BOTH, expand = 1)

lblTitle = tk.Label(
    master=frmTitle,
    text='текст',
    anchor='center',
    relief=tk.RAISED,
    borderwidth=1,
    height = 2
)
lblTitle.pack(fill=tk.X)

lbl1 = tk.Label(
    master=frmTitle,
    text= 'Название образовательного учреждения',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl1.pack(side = tk.LEFT, fill='both', expand=True)
lbl2 = tk.Label(
    master=frmTitle,
    text= 'Проектирование нейроинтерфейсов',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl2.pack(side = tk.LEFT, fill='both', expand=True)
lbl3 = tk.Label(
    master=frmTitle,
    text= 'Фофанов Максим',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl3.pack(side = tk.LEFT, fill='both', expand=True)

frmTitle1 = tk.Frame(master=frmDivTitle)
frmTitle1.pack(side = tk.LEFT, fill = tk.BOTH)

lblTitle1 = tk.Label(
    master=frmTitle1,
    text='текст',
    anchor='center',
    relief=tk.RAISED,
    borderwidth=1,
    height = 2
)
lblTitle1.pack(fill=tk.X)

lbl4 = tk.Label(
    master=frmTitle1,
    text= 'Фофанов Максим sdf dsf sdfsdf sdfdsadsadasdsd',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=100
)
lbl4.pack(side = tk.LEFT, fill='both', expand=True)

frmDiv = tk.Frame(root)
frmDiv.pack(fill = tk.BOTH, expand = 1)

frmDivContent = tk.Frame(frmDiv)
frmDivContent.pack(side = tk.LEFT,  fill = tk.BOTH, expand = 1)

frmDivGraph = tk.Frame(frmDivContent)
frmDivGraph.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)




frmInfo = tk.Frame(frmDivContent, pady= 10, padx = 10, relief=tk.RAISED, borderwidth=1)
frmInfo.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = 1)

txtInfo = tk.Text(frmInfo)
txtInfo.insert(tk.END, 'info')
txtInfo.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = 1)

frmVideo = tk.Frame(frmDiv, pady= 10, padx= 100, relief=tk.RAISED, borderwidth=1)
frmVideo.pack(side = tk.RIGHT, fill = tk.BOTH, expand = 1)

lblVideo = tk.Label(frmVideo, text='Видео', anchor='center')
lblVideo.pack(fill = tk.BOTH, expand = 1)


plotter = SerialPlotter(root, frmDivGraph, MAXLEN, PORT, BAUDRATE)
root.protocol("WM_DELETE_WINDOW", plotter.on_close)
root.mainloop()