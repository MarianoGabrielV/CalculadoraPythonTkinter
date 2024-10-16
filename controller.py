# controller.py

from model import CalculatorModel
from view import CalculatorView
import tkinter as tk

class CalculatorController:
    def __init__(self, root):
        self.model = CalculatorModel()
        self.view = CalculatorView(root)

        # Asignar la función de clic de botón
        self.view.on_button_click = self.handle_button_click

    def handle_button_click(self, button_text):
        current_text = self.view.result_var.get()

        if button_text == 'C':
            self.view.clear()
        elif button_text == '=':
            try:
                result = self.model.evaluate(current_text)
                self.view.set_result(result)
            except Exception:
                self.view.set_result("Error")
        else:
            new_text = current_text + button_text
            self.view.set_result(new_text)

        # Manejo de nuevas funciones (cuando sea necesario)
        if button_text == 'sqrt':
            try:
                number = float(current_text)
                result = self.model.sqrt(number)
                self.view.set_result(result)
            except ValueError:
                self.view.set_result("Error")
        elif button_text == 'power':
            # Asume que el usuario ingresará algo como "2 3" para 2^3
            try:
                base, exponent = map(float, current_text.split())
                result = self.model.power(base, exponent)
                self.view.set_result(result)
            except ValueError:
                self.view.set_result("Error")
        elif button_text == 'sin':
            try:
                number = float(current_text)
                result = self.model.sin(number)
                self.view.set_result(result)
            except ValueError:
                self.view.set_result("Error")
        elif button_text == 'cos':
            try:
                number = float(current_text)
                result = self.model.cos(number)
                self.view.set_result(result)
            except ValueError:
                self.view.set_result("Error")
        elif button_text == 'tan':
            try:
                number = float(current_text)
                result = self.model.tan(number)
                self.view.set_result(result)
            except ValueError:
                self.view.set_result("Error")
        elif button_text == 'log':
            try:
                number = float(current_text)
                result = self.model.log(number)
                self.view.set_result(result)
            except ValueError:
                self.view.set_result("Error")
        elif button_text == 'factorial':
            try:
                number = int(float(current_text))  # Asegúrate de que sea un entero
                result = self.model.factorial(number)
                self.view.set_result(result)
            except ValueError:
                self.view.set_result("Error")
            except OverflowError:
                self.view.set_result("Error")  # Para números muy grandes

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorController(root)
    root.mainloop()
