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
        p1 = Home(self)
        p2 = Load(self)
        p3 = Create(self)
        
        buttonframe = tkinter.Frame(self)
        container = tkinter.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        b1 = tkinter.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tkinter.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tkinter.Button(buttonframe, text="Page 3", command=p3.lift)
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        p1.lift()

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