import tkinter as tk
import tkinter.ttk as ttk
from topo import *
from globals import AUTHOR


class ConfigFrame(ttk.Frame):
    def __init__(self, top):
        ttk.Frame.__init__(self, top)
        value = tk.IntVar()
        value.set(top.ENTIRE_CIRCLE_ANGLE)
        value.trace(
            "w", lambda name, mode, index, value=value: self.change_value(value))
        ttk.Label(self, text="Miara kąta pełnego").grid(
            sticky="W", pady=5, padx=5)
        angle = ttk.Entry(self, textvariable=value)
        angle.grid(column=0, row=1, pady=5, padx=5)

        author = tk.Label(self, text="Autor: " + AUTHOR, wrap=200)
        author.grid(column=1, row=0, rowspan=2)

    def change_value(self, value):
        value = value.get()
        try:
            value = int(value)
        except ValueError:
            pass
        else:
            if value > 0:
                ZGZ.set_circle_angle(value)
                ZGO.set_circle_angle(value)
