import tkinter

class Page(tkinter.Frame):
    
    def __init__(self, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)

    def registerPage(self, pageName, pageObj):
        setattr(self, pageName, pageObj)

    def moveToPage(self, pageName):
        try:
            getattr(self, pageName).lift()
            getattr(self, pageName).update()
        except AttributeError:
            print(__name__ + ": missing '" + pageName + "'. Did you register it?")