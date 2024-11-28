class Calculadora:
    def __init__(self):
        pass
    def soma(self, x, y):
        variavel= x + y
        return variavel
    def subtracao(self, x, y):
        variavel= x - y
        return variavel
    def multiplicar(self, x, y):
        variavel= x * y
        return variavel
    def dividir(self, x, y):
        if y == 0:
            raise ZeroDivisionError('este numero n é dividido') 
        variavel= x/y
        return variavel