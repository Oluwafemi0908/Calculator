from tkinter import *


def add(n1, n2): return n1 + n2
def subtract(n1, n2): return n1 - n2
def multiply(n1, n2): return n1 * n2
def divide(n1, n2): return n1 / n2 if n2 != 0 else "Error"


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title('Calculator')
        self.window.minsize(300, 500)
        self.window.config(padx=10, pady=20)

        self.screen = Entry(width=15, font=("Arial", 25), bg="lightblue", fg="black", justify="right")
        self.screen.insert(END, '0')
        self.screen.grid(row=0, column=0, columnspan=5, ipadx=30, ipady=10)

        self.ans_screen = Entry(width=10, font=("Arial", 15), bg="lightblue", fg="black", justify="right")
        self.ans_screen.insert(END, '0')
        self.ans_screen.grid(row=1, column=0, columnspan=5, ipadx=30)

        self.buttons = [
            [7, 8, 9, 'Del', 'AC'],
            [4, 5, 6, 'x', '÷'],
            [1, 2, 3, '+', '-'],
            [0, '00','.', 'Ans', '=']
        ]

        self.num1 = None
        self.operator = None
        self.ans = 0
        self.operators = {
            "+": add,
            "-": subtract,
            "x": multiply,
            "÷": divide
        }

        self.create_buttons()

    def create_buttons(self):
        for row_idx, row in enumerate(self.buttons, start=2):
            for col_idx, val in enumerate(row):
                button = Button(
                    text=val,
                    width=5,
                    height=2,
                    font=("Arial", 14),
                    command=lambda v=val: self.button_actions(v)
                )
                button.grid(row=row_idx, column=col_idx, padx=5, pady=5)

    def button_actions(self, value):
        current = self.screen.get()

        if value == 'AC':
            self.screen.delete(0, END)
            self.screen.insert(END, '0')
            self.num1 = None
            self.operator = None

        elif value == 'Del':
            if len(current) > 1:
                self.screen.delete(len(current)-1, END)
            else:
                self.screen.delete(0, END)
                self.screen.insert(END, '0')

        elif value == '=':
            if self.operator and self.num1 is not None:
                try:
                    num2 = float(self.screen.get())
                    result = self.operators[self.operator](self.num1, num2)
                    self.ans = result
                    self.screen.delete(0, END)
                    self.screen.insert(END, str(result))
                    self.ans_screen.delete(0, END)
                    self.ans_screen.insert(END, str(result))
                    self.operator = None
                    self.num1 = None
                except:
                    self.screen.delete(0, END)
                    self.screen.insert(END, 'Error')

        elif value in self.operators:
            self.num1 = float(current)
            self.operator = value
            self.screen.delete(0, END)
            self.screen.insert(END, '0')

        elif value == 'Ans':
            self.screen.delete(0, END)
            self.screen.insert(END, str(self.ans))

        elif value == '.':
            self.screen.insert(END, str('.'))

        else:
            if current == '0':
                self.screen.delete(0, END)
            self.screen.insert(END, str(value))

    def run(self):
        self.window.mainloop()


UI().run()
