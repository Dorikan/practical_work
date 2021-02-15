import os
dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)

from gui import gui
import tkinter as tk

root = tk.Tk()
app = gui(master=root)
app.mainloop()