import tkinter

class Load(tkinter.Frame):
   def __init__(self, *args, **kwargs):
       tkinter.Frame.__init__(self, *args, **kwargs)
       label = tkinter.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)