import queue
import serial
import struct
import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from collections import deque
from threading import Thread



class SerialPlotter:
    def __init__(self, root, container, maxlen: int, port: str, baudrate: int):
        self.root = root
        self.container = container

        self.data1 = deque(maxlen=maxlen)
        self.data2 = deque(maxlen=maxlen)
        self.queue = queue.Queue()

        self.running = True
        # self.iter = 0

        self.ser = serial.Serial(port, baudrate)
        self.thread = Thread(target=self.listen_serial)
        self.thread.start()

        self.setup_gui()
        self.update_plot()

    def setup_gui(self):
        frmGraphEKG = tk.Frame(self.container, pady=10, padx=10, relief=tk.RAISED, borderwidth=1)
        frmGraphEKG.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        fig1 = Figure(figsize=(2, 2))
        self.ax1 = fig1.add_subplot(111)
        self.line1, = self.ax1.plot([], [])

        self.ax1.set_ylim(0, 1024)

        self.canvas1 = FigureCanvasTkAgg(fig1, master=frmGraphEKG)
        self.canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=1)

        frmGraphEMG = tk.Frame(self.container, pady=10, padx=10, relief=tk.RAISED, borderwidth=1)
        frmGraphEMG.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        fig2 = Figure(figsize=(2, 2))
        self.ax2 = fig2.add_subplot(111)
        self.line2, = self.ax2.plot([], [])

        self.ax2.set_ylim(0, 1024)

        self.canvas2 = FigureCanvasTkAgg(fig2, master=frmGraphEMG)
        self.canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=1)

    def listen_serial(self):
        while self.running:
            try:
                # Чтение строки вместо бинарных данных
                line = self.ser.readline().decode('latin-1').strip()
                data1, data2 = map(int, line.split(','))
                self.queue.put((data1, data2))
            except:
                ...


    def update_plot(self):


        try:
            while True:
                num1, num2 = self.queue.get_nowait()
                self.data1.append(num1)
                # self.data2.append(map_num(num1, 0, 1024, -1.0, -1.0)) # Инвертированный первый пин
                self.data2.append(num2)
                # self.iter += 1
        except queue.Empty:
            ...

        # self.line1.set_data(range(self.iter+1-len(self.data1), self.iter+1), self.data1)
        self.line1.set_data(range(1, len(self.data1)+1), self.data1)
        self.ax1.relim()
        self.ax1.autoscale_view(scaley=False)
        self.canvas1.draw()

        # self.line2.set_data(range(self.iter+1-len(self.data2), self.iter+1), self.data2)
        self.line2.set_data(range(1, len(self.data2)+1), self.data2)
        self.ax2.relim()
        self.ax2.autoscale_view(scaley=False)
        self.canvas2.draw()

        self.root.after(100, self.update_plot)

    def on_close(self):
        self.running = False
        self.thread.join()
        self.ser.close()
        self.root.destroy()