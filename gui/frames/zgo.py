import tkinter.ttk as ttk
from ..input_table import InputTable
from ..func import *
from topo import *


class ZGOFrame(ttk.Frame):
    def __init__(self, top):
        ttk.Frame.__init__(self, top)
        container_1 = ttk.Frame(self)
        container_1.grid(row=0, sticky="W")
        variables = ("A", "B", "Kz")
        self.input = InputTable(container_1, variables)

        exe_btn = ttk.Button(self,
                             text="Oblicz -->",
                             command=lambda: self.cal_ZGO())
        exe_btn.grid(column=1, row=0)

        container_2 = ttk.Frame(self)
        variables = ("d", "kp(Kz)")
        self.output = InputTable(container_2, variables)
        container_2.grid(row=0, column=2, sticky="W")

    def cal_ZGO(self):
        inputs = get_values(self.input)
        A_cords = str(inputs["A"])
        B_cords = str(inputs["B"])
        Kz = int(inputs["Kz"])
        zgo = ZGO(A_cords, B_cords, Kz)
        d, kp = zgo.get_results()
        values = {"d": d,
                  "kp(Kz)": kp}
        insert_values(self.output, values)

