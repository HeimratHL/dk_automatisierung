import tkinter
import globalVars
from pages.page import Page

class Home(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        tkinter.Frame.rowconfigure(self, 0, weight=1)
        tkinter.Frame.rowconfigure(self, 1, weight=1)
        tkinter.Frame.rowconfigure(self, 2, weight=1)
        tkinter.Frame.rowconfigure(self, 3, weight=1)
        tkinter.Frame.columnconfigure(self, 0, weight=1)
        tkinter.Label(self, text="Startseite").grid(row=0)
        tkinter.Button(self, text="Load Preset", command=lambda:self.moveToPage("loadPage")).grid(row=1)
        tkinter.Button(self, text="Create Preset", command=lambda:self.moveToPage("createPage")).grid(row=2)
        self.currentPreset = tkinter.Label(self, text=globalVars.currentPreset)
        self.currentPreset.grid(row=3)
    
    def update(self):
        self.currentPreset.configure(text=globalVars.currentPreset)
        