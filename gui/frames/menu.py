import tkinter.ttk as ttk


class MenuFrame(ttk.Frame):
    def __init__(self, top, frames):
        ttk.Frame.__init__(self, top)
        self.frames = frames
        self.top = top
        zgo_btn = ttk.Button(self)
        zgo_btn.configure(text="ZGO",
                          command=lambda: self.change_frame(frames[0]))
        zgo_btn.grid()
        zgz_btn = ttk.Button(self)
        zgz_btn.configure(text="ZGZ",
                          command=lambda: self.change_frame(frames[1]))
        zgz_btn.grid(column=1, row=0)
        draft_btn = ttk.Button(self)
        draft_btn.configure(text="Ciąg",
                            command=lambda: self.change_frame(frames[2]))
        draft_btn.grid(column=2, row=0)
        config_btn = ttk.Button(self)
        config_btn.configure(text="Konfiguracja",
                             command=lambda: self.change_frame(frames[3]))
        config_btn.grid(column=3, row=0)

    def change_frame(self, new_frame):
        for frame in self.frames:
            frame.grid_forget()
        new_frame.grid(column=0, row=1, sticky="W")
