def potencia(valor, expoente):
    if expoente == 0:
        return 1
    else:
        return valor * potencia(valor, expoente-1)
def factory(valor):
    if valor == 1  or valor == 0:
        return 1
    else:
        return valor * factory(valor-1)  
def dividindo(valor, divisor):
    if valor <= divisor:
        return 0
    else:
        return 1 + dividindo(valor - divisor, divisor) 
        