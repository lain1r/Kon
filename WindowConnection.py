import tkinter as tk
from tkinter import *

# pip install pyserial

root = tk.Tk()
root.title('окно')
root.geometry('1024x768')
root.resizable(width=False, height=False)

ekgConnect = 0
emgConnect = 0

if ekgConnect == 1:
    textConnect = "Пульс определен, перейдите к подключению электродов для исследования ЭМГ"
else:
    textConnect = "Пульс не определен проверьте подключение"

if emgConnect == 1:
    textConnect1 = "Пульс определен, перейдите к подключению электродов для исследования ЭМГ"
else:
    textConnect1 = "Пульс не определен проверьте подключение"


# Верхний фрейм с заголовком
frmTitle = tk.Frame(master=root, relief=tk.RAISED, borderwidth=1)
frmTitle.pack(fill='x')

lblTitle = tk.Label(
    master=frmTitle,
    text='текст',
    anchor='center',
    height = 2
)
lblTitle.pack(fill=tk.X, expand=True)

frmText = tk.Frame(master= root)
frmText.pack(fill=tk.BOTH)

lbl1 = tk.Label(
    master=frmText,
    text= 'Название образовательного учреждения',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl1.pack(side = tk.LEFT, fill='both', expand=True)
lbl2 = tk.Label(
    master=frmText,
    text= 'Проектирование нейроинтерфейсов',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl2.pack(side = tk.LEFT, fill='both', expand=True)
lbl3 = tk.Label(
    master=frmText,
    text= 'Фофанов Максим',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200
)
lbl3.pack(side = tk.LEFT, fill='both', expand=True)

frmTitle2 = tk.Frame(master=root, relief=tk.RAISED, borderwidth=1)
frmTitle2.pack(fill='x')

lblTitle2 = tk.Label(
    master=frmTitle2,
    text='текст',
    anchor='center',
    height = 2
)
lblTitle2.pack(fill=tk.X, expand=True)

frmConn = tk.Frame(master= root)
frmConn.pack(side = tk.LEFT, fill=tk.BOTH, expand=True)

frmGraph = tk.Frame(master= root)
frmGraph.pack(side = tk.RIGHT, fill=tk.BOTH, expand=True)

lblConn = tk.Label(
    master=frmConn,
    text= textConnect,
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200)
lblConn.pack(side=tk.TOP, fill='both', expand=True)

# imgEKG = PhotoImage(file='photo.png')
#
# imageEKG = Canvas(frmConn)
# imageEKG.create_image(100,190, anchor = tk.CENTER, image = imgEKG)
# imageEKG.pack(side=tk.LEFT, fill='both', expand = 1)

lblGraph = tk.Label(
    master=frmGraph,
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200)
lblGraph.pack(side=tk.TOP, fill='both', expand=True)


lblConn1 = tk.Label(
    master=frmConn,
    text= textConnect1,
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200)
lblConn1.pack(side=tk.BOTTOM, fill='both', expand=True)

lblGraph1 = tk.Label(
    master=frmGraph,
    text= 'Фофанов Максим',
    relief=tk.RAISED,
    borderwidth=1,
    anchor='center',
    wraplength=200)
lblGraph1.pack(side=tk.BOTTOM, fill='both', expand=True)

root.mainloop()