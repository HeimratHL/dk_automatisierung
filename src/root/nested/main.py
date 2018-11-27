import tkinter
import argparse
from pages.home import Home
from pages.load import Load
from pages.create import Create

## Globals ##
title = "Heimrat Preislisten-Tool"

class Main(tkinter.Frame):
    def __init__(self, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)
        ## Pages ##
        loadPage = Load(self)
        createPage = Create(self)
        homePage = Home(self, loadPage, createPage)
        ## Building the page container ##
        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        homePage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        loadPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        createPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ## Show home page by default ##
        homePage.lift()

## Argument Parsing ##
parser = argparse.ArgumentParser(description=title)
parser.add_argument('--resolution', help='sets application gui size, provide string like 320x200', required=True)
parser.add_argument('--fullscreen', help='fullscreens the application, default: False', default=False)
args = parser.parse_args()

## GUI init ##
window = tkinter.Tk()
main = Main(window)                                         #put main frame into window
main.pack(side="top", fill="both", expand=True)
window.attributes("-fullscreen", args.fullscreen)
#window.overrideredirect(1)                                 #removes window title bar
window.geometry(args.resolution)
window.title(title)
window.mainloop()