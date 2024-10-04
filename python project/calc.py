import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create entry field for user input
        self.entry_field = tk.Entry(master, width=35, borderwidth=5)
        self.entry_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create number buttons
        buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', '.', '='
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(master, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

        # Create operator buttons
        operators = [
            '+', '-', '*', '/'
        ]
        row_val = 1
        for operator in operators:
            tk.Button(master, text=operator, width=5, command=lambda operator=operator: self.click_operator(operator)).grid(row=row_val, column=3)
            row_val += 1

        # Create clear button
        tk.Button(master, text="Clear", width=22, command=self.clear).grid(row=4, column=0, columnspan=4)

    def click_button(self, button):
        current = self.entry_field.get()
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(0, str(current) + str(button))

    def click_operator(self, operator):
        current = self.entry_field.get()
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(0, str(current) + str(operator))

    def clear(self):
        self.entry_field.delete(0, tk.END)

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()