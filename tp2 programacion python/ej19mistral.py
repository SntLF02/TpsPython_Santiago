class OperacionMatematica:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def sumarNumeros(self):
        return self.valor1 + self.valor2

    def restarNumeros(self):
        return self.valor1 - self.valor2

    def multiplicarNumeros(self):
        return self.valor1 * self.valor2

    def dividirNumeros(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero"

    def aplicarOperacion(self, operacion):
        if operacion == '+':
            return self.sumarNumeros()
        elif operacion == '-':
            return self.restarNumeros()
        elif operacion == '*':
            return self.multiplicarNumeros()
        elif operacion == '/':
            return self.dividirNumeros()
        else:
            return "Operación no válida"

class Calculo:
    @staticmethod
    def main():
        operacion = OperacionMatematica(10, 5)

        operaciones = ['+', '-', '*', '/']
        for op in operaciones:
            resultado = operacion.aplicarOperacion(op)
            print(f"Resultado de la operación '{op}': {resultado}")

# Ejecutar el método main de la clase Calculo
Calculo.main()