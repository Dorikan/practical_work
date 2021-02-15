import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import analyzer

class gui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        ###args
        self.file_name = None
        self.input_from_gui_btn = None
        self.file_output_btn = None
        self.input_file_btn = None
        self.output_widget = None
        self.text = None
        ###args

        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.output_widget = tk.Text(self.master, state='normal', width=40, height=20)

        self.input_file_btn = tk.Button(self.master, height=10, width=25)
        self.file_output_btn = tk.Button(self.master, height=10, width=25)
        self.input_from_gui_btn = tk.Button(self.master, height=10)

        self.input_file_btn["text"] = "Открыть файл для анализа."
        self.input_file_btn["command"] = self.input_file_button_command
        self.file_output_btn["text"] = "Сохранить информацию в файл."
        self.file_output_btn["command"] = self.output_file_button_command
        self.input_from_gui_btn["text"] = "ввести информацию из поля ввода"
        self.input_from_gui_btn["command"] = self.gui_input

        self.output_widget.grid(row=0, column=1, sticky='we', rowspan=2)
        self.input_file_btn.grid(row=0, column=0, sticky='nw')
        self.input_from_gui_btn.grid(row=0, column=2, rowspan=2)

    def input_file_button_command(self):
        self.file_name = fd.askopenfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        self.gui_output(text_or_file='file')
    def gui_input(self):
        self.text = self.output_widget.get(1.0, tk.END)
        self.gui_output(text_or_file='text')

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

    def gui_output(self, text_or_file=None):
        if text_or_file == 'file':
            self.text = self.analysis(from_file=True)
        elif text_or_file == 'text':
            self.text = self.analysis(from_text=True)
        elif text_or_file is None:
            self.analysis(False, False)
        self.output_widget.insert(1.0, self.text[1:])
        self.output_widget.config(state='disabled')
        self.hidden_widgets()

    def analysis(self, from_file=False, from_text=False):
        temp = None
        if from_file:
            if self.file_name == "":
                mb.showerror("Error",
                             "Вы не указали текстовый файл.")
            else:
                temp = analyzer.analyzer(file=self.file_name)
        elif from_text:
            temp = analyzer.analyzer(text=self.text)
        elif (from_text is None) and (from_file is None):
            mb.showerror("Error",
                         "Вы не указали текстовый файл/не написали текст.")

        if temp is not None:
            temp.start()
            return temp.gui_otput()
