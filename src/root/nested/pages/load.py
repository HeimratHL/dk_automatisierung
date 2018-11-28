import tkinter
import glob
from pages.page import Page

presetFiles = glob.glob(".\presets\*.html")
scrollCounter = 0

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
        tkinter.Button(self, text="Up", command=lambda:self.scrollUp()).grid(row=1, column=0)
        tkinter.Button(self, text="Down", command=lambda:self.scrollDown()).grid(row=4, column=0)
        tkinter.Button(self, text="empty").grid(row=1, column=1, sticky=tkinter.W)
        tkinter.Button(self, text="empty").grid(row=2, column=1, sticky=tkinter.W)
        tkinter.Button(self, text="empty").grid(row=3, column=1, sticky=tkinter.W)
        tkinter.Button(self, text="empty").grid(row=4, column=1, sticky=tkinter.W)
        self.loadPresets()
    
    def scrollUp(self):
        global scrollCounter
        if scrollCounter > 0:
            scrollCounter = scrollCounter - 1
            self.loadPresets()

    def scrollDown(self):
        global scrollCounter
        if scrollCounter + 4 < len(presetFiles):
            scrollCounter = scrollCounter + 1
            self.loadPresets()

    def loadPresets(self):
        for num, name in enumerate(presetFiles[scrollCounter:scrollCounter + 4]):
            tkinter.Button(self, text="{}: {}".format(num, name), command=lambda:print("test")).grid(row=num + 1, column=1, sticky=tkinter.W)