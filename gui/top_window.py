import tkinter.ttk as ttk
from .frames import *


class TopoWindow(ttk.Frame):
    def __init__(self, top):
        ttk.Frame.__init__(self, top)
        self.ENTIRE_CIRCLE_ANGLE = 6000
        frames = [ZGOFrame(self),
                  ZGZFrame(self),
                  DraftFrame(self),
                  ConfigFrame(self)]
        menu = MenuFrame(self, frames)
        menu.grid()
        frames[0].grid(row=1, sticky="W")
