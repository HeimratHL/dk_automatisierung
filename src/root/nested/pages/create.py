import tkinter

class Create(tkinter.Frame):
   def __init__(self, *args, **kwargs):
       tkinter.Frame.__init__(self, *args, **kwargs)
       label = tkinter.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)