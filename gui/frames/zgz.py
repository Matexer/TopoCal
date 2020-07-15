import tkinter.ttk as ttk
from ..input_table import InputTable
from ..func import *
from topo import *


class ZGZFrame(ttk.Frame):
    def __init__(self, top):
        ttk.Frame.__init__(self, top)
        container_1 = ttk.Frame(self)
        container_1.grid(row=0, sticky="W")
        variables = ("A", "d", "T")
        self.input = InputTable(container_1, variables)

        exe_btn = ttk.Button(self,
                             text="Oblicz -->",
                             command=lambda: self.cal_ZGZ())
        exe_btn.grid(column=1, row=0)

        container_2 = ttk.Frame(self)
        variables = ("B",)
        self.output = InputTable(container_2, variables)
        container_2.grid(row=0, column=2, sticky="W")

    def cal_ZGZ(self):
        inputs = get_values(self.input)
        A_cords = str(inputs["A"])
        d = int(inputs["d"])
        T = int(inputs["T"])
        zgz = ZGZ(A_cords, T, d)
        B_cords = zgz.get_results()
        values = {"B": B_cords}
        insert_values(self.output, values)
