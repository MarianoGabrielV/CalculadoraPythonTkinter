# model.py

import math

class CalculatorModel:
    def evaluate(self, expression):
        try:
            # Permitir solo operaciones básicas para la seguridad
            allowed_operators = set('0123456789+-*/(). ')
            if any(char not in allowed_operators for char in expression):
                raise ValueError("Caracter no permitido en la expresión")

            result = eval(expression)
            return result
        except Exception:
            return "Error"

    def sqrt(self, x):
        return math.sqrt(x)

    def power(self, base, exponent):
        return base ** exponent

    def sin(self, x):
        return math.sin(math.radians(x))

    def cos(self, x):
        return math.cos(math.radians(x))

    def tan(self, x):
        return math.tan(math.radians(x))

    def log(self, x):
        return math.log10(x)

    def factorial(self, x):
        if x < 0:
            raise ValueError("No se puede calcular el factorial de un número negativo")
        elif x == 0:
            return 1
        else:
            result = 1
            for i in range(1, x + 1):
                result *= i
            return result
