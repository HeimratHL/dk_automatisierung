import tkinter

class Home(tkinter.Frame):
   def __init__(self, *args, **kwargs):
       tkinter.Frame.__init__(self, *args, **kwargs)
       label = tkinter.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)