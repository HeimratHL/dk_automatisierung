import tkinter
import argparse

## Argument Parsing ##
parser = argparse.ArgumentParser(description='Heimrat Preislisten-Tool')
parser.add_argument('--resolution', help='sets application gui size, provide string like 320x200', required=True)
parser.add_argument('--fullscreen', help='fullscreens the application, default: False', default=False)
args = parser.parse_args()

window = tkinter.Tk()
window.attributes("-fullscreen", args.fullscreen)
window.geometry(args.resolution)
window.title("test")
window.mainloop()