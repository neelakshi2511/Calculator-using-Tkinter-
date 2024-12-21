#calcultor GUI using Tkinter 

import tkinter as tk
from functools import partial


class Calculator:
    def __init__(self, root):
        self.btns_frame = None
        self.root = root
        self.root.title("Neelakshi's Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_input_frame()
        self.create_buttons_frame()
        self.create_buttons()

    def create_input_frame(self):
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black",
                               highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50,
                               bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

    def create_buttons_frame(self):
        self.btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        self.btns_frame.pack()

    def create_buttons(self):
        btn_cfg = {'fg': 'black', 'width': 10, 'height': 4, 'bd': 1, 'relief': 'solid', 'cursor': 'hand2'}

        buttons = [
            ("C", "#ADD8E6", 0, 0, 2, self.clear_display), ("(", "yellow", 0, 2, 1, partial(self.btn_click, "(")),
            (")", "yellow", 0, 3, 1, partial(self.btn_click, ")")),
            ("7", "#d0f2a0", 1, 0, 1, partial(self.btn_click, "7")),
            ("8", "#d0f2a0", 1, 1, 1, partial(self.btn_click, "8")),
            ("9", "#d0f2a0", 1, 2, 1, partial(self.btn_click, "9")),
            ("/", "#f2d7a0", 1, 3, 1, partial(self.btn_click, "/")),
            ("4", "#d0f2a0", 2, 0, 1, partial(self.btn_click, "4")),
            ("5", "#d0f2a0", 2, 1, 1, partial(self.btn_click, "5")),
            ("6", "#d0f2a0", 2, 2, 1, partial(self.btn_click, "6")),
            ("*", "#f2d7a0", 2, 3, 1, partial(self.btn_click, "*")),
            ("1", "#d0f2a0", 3, 0, 1, partial(self.btn_click, "1")),
            ("2", "#d0f2a0", 3, 1, 1, partial(self.btn_click, "2")),
            ("3", "#d0f2a0", 3, 2, 1, partial(self.btn_click, "3")),
            ("-", "#f2d7a0", 3, 3, 1, partial(self.btn_click, "-")),
            ("0", "#d0f2a0", 4, 0, 2, partial(self.btn_click, "0")),
            (".", "#f2d7a0", 4, 2, 1, partial(self.btn_click, ".")),
            ("+", "#f2d7a0", 4, 3, 1, partial(self.btn_click, "+")), ("=", "#ADD8E6", 5, 0, 4, self.calculate)
        ]

        for (text, color, row, col, colspan, command) in buttons:
            tk.Button(self.btns_frame, text=text, bg=color, command=command, **btn_cfg).grid(row=row, column=col,
                                                                                             columnspan=colspan,
                                                                                             sticky='nsew')

        for i in range(5):
            self.btns_frame.grid_rowconfigure(i, weight=1)
            self.btns_frame.grid_columnconfigure(i, weight=1)

    def btn_click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear_display(self):
        self.expression = ""
        self.input_text.set("")

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result  # Keep the result for further calculations
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
