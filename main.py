import tkinter as tk
from globals import *
from gui import TopoWindow

if __name__ == "__main__":
    root = tk.Tk()
    root.title(TITLE)
    frame = TopoWindow(root)
    frame.grid()
    root.mainloop()
