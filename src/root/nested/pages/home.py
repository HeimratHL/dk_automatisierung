import tkinter

class Home(tkinter.Frame):
    def __init__(self, master, loadPage, createPage):
        tkinter.Frame.__init__(self, master)
        #tkinter.Frame.configure(self, background="black")
        tkinter.Frame.rowconfigure(self, 0, weight=1)
        tkinter.Frame.rowconfigure(self, 1, weight=1)
        tkinter.Frame.rowconfigure(self, 2, weight=1)
        tkinter.Frame.rowconfigure(self, 3, weight=1)
        tkinter.Frame.columnconfigure(self, 0, weight=1)
        tkinter.Label(self, text="Startseite").grid(row=0)
        tkinter.Button(self, text="Load Preset", command=lambda:loadPage.lift()).grid(row=1)
        tkinter.Button(self, text="Create Preset", command=lambda:createPage.lift()).grid(row=2)
        tkinter.Label(self, text="active: ...............TODO..............").grid(row=3)