import tkinter as tk
from tkinter import filedialog as fd
import analyzer

class gui(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        ###args
        self.file_name = None
        self.input_file = None
        ###args

        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_file = tk.Button(self)
        self.input_file["text"] = "Открыть файл для анализа"
        self.input_file["command"] = self.input_file_button_command
        self.input_file.pack(side="top")

    def input_file_button_command(self):
        self.file_name = fd.askopenfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        x = self.analysis()
        print(x)

    def analysis(self):
        temp = analyzer.analyzer(self.file_name)
        temp.start()
        return temp.gui_otput()

root = tk.Tk()
app = gui(master=root)
app.mainloop()