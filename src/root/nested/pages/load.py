import tkinter
from pages.page import Page

class Load(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        tkinter.Frame.rowconfigure(self, 0, weight=1)
        tkinter.Frame.rowconfigure(self, 1, weight=1)
        tkinter.Frame.rowconfigure(self, 2, weight=1)
        tkinter.Frame.rowconfigure(self, 3, weight=1)
        tkinter.Frame.rowconfigure(self, 4, weight=1)
        tkinter.Frame.columnconfigure(self, 0, weight=0)
        tkinter.Frame.columnconfigure(self, 1, weight=1)
        tkinter.Label(self, text="Load Preset").grid(row=0, column=1, sticky=tkinter.NE, padx=10, pady=10)
        tkinter.Button(self, text="Back", command=lambda:self.moveToPage("homePage")).grid(row=0, column=0, sticky=tkinter.NW, padx=10, pady=10)
        tkinter.Button(self, text="Up", command=lambda:print("up")).grid(row=1, column=0)
        tkinter.Button(self, text="Down", command=lambda:print("down")).grid(row=4, column=0)
        tkinter.Button(self, text="Preset1", command=lambda:print("fake")).grid(row=1, column=1, sticky=tkinter.W)
        tkinter.Button(self, text="Preset2", command=lambda:print("fake")).grid(row=2, column=1, sticky=tkinter.W)
        tkinter.Button(self, text="Preset3", command=lambda:print("fake")).grid(row=3, column=1, sticky=tkinter.W)
        tkinter.Button(self, text="Preset3", command=lambda:print("fake")).grid(row=4, column=1, sticky=tkinter.W)