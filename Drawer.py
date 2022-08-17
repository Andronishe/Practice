import tkinter as tk


class Drawer(tk.Tk):
    def __init__(self, wd, hgt):
        super().__init__()
        self.title("Казалось бы, при чем здесь самара?")
        self.canvas = tk.Canvas(self, bg="white", width=wd, height=hgt)
        self.canvas.pack()

    def draw(self, x, y, color):
        self.canvas.create_rectangle((x, y) * 2, outline="", fill=color)
        self.canvas.pack()
