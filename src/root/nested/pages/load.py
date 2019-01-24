import tkinter
import glob
import globalVars
from pages.page import Page

presetFiles = glob.glob("./presets/*.html")
scrollCounter = 0

class Load(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        tkinter.Frame.rowconfigure(self, 0, weight=1)
        tkinter.Frame.rowconfigure(self, 1, weight=1)
        tkinter.Frame.rowconfigure(self, 2, weight=1)
        tkinter.Frame.rowconfigure(self, 3, weight=1)
        tkinter.Frame.rowconfigure(self, 4, weight=1)
        tkinter.Frame.rowconfigure(self, 5, weight=1)
        tkinter.Frame.rowconfigure(self, 6, weight=1)
        tkinter.Frame.columnconfigure(self, 0, weight=0)
        tkinter.Frame.columnconfigure(self, 1, weight=1)
        tkinter.Label(self, text="Load Preset").grid(row=0, column=1, sticky=tkinter.NE, padx=10, pady=10)
        tkinter.Button(self, text="Back", command=lambda:self.moveToPage("homePage")).grid(row=0, column=0, sticky=tkinter.NW, padx=10, pady=10)
        tkinter.Button(self, text="Up", command=lambda:self.scrollUp()).grid(row=1, column=0)
        tkinter.Button(self, text="Down", command=lambda:self.scrollDown()).grid(row=4, column=0)
        self.currentPreset = tkinter.Label(self, text=globalVars.currentPreset)
        self.currentPreset.grid(row=6, column=1, sticky = tkinter.NW, padx=10, pady=10)
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
            tkinter.Button(self, text="{}: {}".format(num, name), command=lambda:self.setCurrentPreset(name)).grid(row=num + 1, column=1, sticky=tkinter.W)
    
    def setCurrentPreset(self, name):
        print(name)
        #globalVars.currentPreset = "Active: " + name
        #self.update()

    def update(self):
        self.currentPreset.configure(text=globalVars.currentPreset)