import tkinter as tk
from Channel import *


class WindowWidgets:
    def __init__(self):
        self.win = tk.Tk()
        self.plane_var = tk.IntVar()
        self.channel_var = tk.IntVar()
        self.final_plane = 0
        self.final_channel = 0

    def select_plane(self):
        self.final_plane = self.plane_var.get()
        return self.final_plane

    def select_channel(self):
        self.final_channel = self.channel_var.get()
        if self.final_channel == 0:
            self.final_channel = Chanel.RED
        elif self.final_channel == 1:
            self.final_channel = Chanel.GREEN
        elif self.final_channel == 2:
            self.final_channel = Chanel.BLUE
        print(self.final_channel)

    def create_window(self):
        self.win.title('1488')
        self.win.geometry('500x300')
        tk.Label(self.win, text='select bit plane').place(x=20, y=0)
        t = 0
        for i in range(8):
            t += 23
            tk.Radiobutton(self.win, text=f'bit plane {i}', variable=self.plane_var,
                           value=i, command=self.select_plane).place(x=20, y=t)
        tk.Label(self.win, text='select channel').pack()

        for i in Chanel:
            tk.Radiobutton(self.win, text=f'channel {i.name}', variable=self.channel_var,
                           value=i.value, command=self.select_channel).pack()
        tk.Button(self.win, text='Get picture', command=self.select_plane).pack(side=tk.BOTTOM)

        self.win.mainloop()


window = WindowWidgets()
window.create_window()



