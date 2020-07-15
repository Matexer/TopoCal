import tkinter as tk
import tkinter.ttk as ttk
from ..input_table import InputTable
from ..func import *
from topo import *


class DraftFrame(ttk.Frame):
    def __init__(self, top):
        ttk.Frame.__init__(self, top)
        self.Point = None
        self.PointNum = 2
        seed_container = ttk.Frame(self)
        seed_container.grid(sticky="W")
        ttk.Label(seed_container, text="1. ").grid()
        self.seed = ttk.Entry(seed_container,
                              width=27)
        self.seed.grid(row=0, column=1)

        list_container = ttk.Frame(self)
        list_container.grid(rowspan=2)
        scrollbar = tk.Scrollbar(list_container)
        scrollbar.pack(side="right", fill="y")
        self.point_list = tk.Listbox(list_container,
                                     yscrollcommand=scrollbar.set,
                                     width=30)
        self.point_list.pack(side="left", fill="both")

        input_container = ttk.Frame(self)
        input_container.grid(column=1, row=0, rowspan=2, sticky="N")
        variables = ("T", "d")
        self.inputs = InputTable(input_container, variables)

        add_btn = ttk.Button(input_container, text="Dodaj",
                             command=lambda: self.add_point())
        add_btn.grid(columnspan=2)
        reset_btn = ttk.Button(self, text="Wyczyść",
                               command=lambda: self.reset())
        reset_btn.grid(sticky="S", column=1, row=2)

    def add_point(self):
        values = get_values(self.inputs)
        T = int(values["T"])
        d = int(values["d"])
        if not self.Point:
            self.Point = self.seed.get()
        zgz = ZGZ(self.Point, T, d)
        self.Point = zgz.get_results()
        self.add_to_list(T, d, self.Point)
        self.clear_entries()

    def add_to_list(self, T, d, point):
        line = f"{self.PointNum}. T: {T}, d: {d} --> {point}"
        self.point_list.insert("end", line)
        self.PointNum += 1

    def clear_entries(self):
        for entry in self.inputs.inputs.values():
            entry.delete(0, 'end')

    def reset(self):
        self.Point = None
        self.PointNum = 2
        self.point_list.delete("0", "end")
