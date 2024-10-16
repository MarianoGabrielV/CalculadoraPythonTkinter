# view.py

import tkinter as tk

class CalculatorView:
    def __init__(self, master):
        self.master = master
        self.master.title("CalcMarianoDev")
        self.master.geometry('400x600+800+200') # Deja que al abrirse se quede en el centro.
        self.master.resizable(False,False) #No se puede expandir, tamaño predeterminado.
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 30), justify="right")
        self.result_entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()
        self.footer_label = tk.Label(self.master, text = 'MarianoDev', font = ('Arial', 12))
        self.footer_label.grid(row=6, column=0, columnspan=4, sticky="e", padx=5) 
        # Inicializa la función on_button_click como None
        self.on_button_click = None

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
            'sqrt', 'sin', 'cos', 'tan',
            'log', 'power', 'factorial'
        ]

        row_value = 1
        col_value = 0
        for button in buttons:
            btn = tk.Button(self.master,bg='#3C3C3C',fg='light sea green', text=button,font = ('',20), command=lambda b=button: self.button_click(b), height=2, width=5)
            btn.grid(row=row_value, column=col_value, sticky="nsew")
            col_value += 1
            if col_value > 3:  # Cambia de fila después de 4 columnas
                col_value = 0
                row_value += 1

        # Configuración de la cuadrícula
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def set_result(self, value):
        self.result_var.set(value)

    def clear(self):
        self.result_var.set("")

    def button_click(self, button):
        # Llama a la función de controlador si se ha definido
        if self.on_button_click:
            self.on_button_click(button)
        else:
            raise NotImplementedError("La función on_button_click debe ser implementada en el controlador")
