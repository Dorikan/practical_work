import tkinter as tk
from tkinter import filedialog as fd
import analyzer

class gui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        ###args
        self.file_name = None
        self.file_output_btn = None
        self.input_file_btn = None
        self.output_widget = None
        self.text = None
        ###args

        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.input_file_btn = tk.Button(self.master, height=10, width=25)
        self.file_output_btn = tk.Button(self.master, height=10, width=25)

        self.input_file_btn["text"] = "Открыть файл для анализа."
        self.input_file_btn["command"] = self.input_file_button_command
        self.file_output_btn["text"] = "Сохранить информацию в файл."
        self.file_output_btn["command"] = self.output_file_button_command

        self.input_file_btn.grid(row=0, column=0, sticky='nw')

    def input_file_button_command(self):
        self.file_name = fd.askopenfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        self.gui_output()

    def output_file_button_command(self):
        file_name = fd.askopenfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        f = open(file_name, 'w')
        f.write(self.text)
        f.close()

    def hidden_widgets(self):
        self.file_output_btn.grid(row=1, column=0, sticky="n")

    def gui_output(self):
        self.text = self.analysis()
        self.output_widget = tk.Text(self.master, state='normal', width=40, height=20)
        self.output_widget.grid(row=0, column=1, sticky='we', rowspan=5)
        # увеличить rowspan при увеличении кол-ва
        # кнопок.
        self.output_widget.insert(1.0, self.text[1:])
        self.output_widget.config(state='disabled')
        self.hidden_widgets()

    def analysis(self):
        temp = analyzer.analyzer(self.file_name)
        temp.start()
        return temp.gui_otput()

root = tk.Tk()
app = gui(master=root)
app.mainloop()