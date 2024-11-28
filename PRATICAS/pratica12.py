from pratica13 import potencia, factory, dividindo
def validar():
    try:
        nota= int(input("digite um valor"))
        if nota >= 0:
           pass
        else:
            raise TypeError("o numero n pode ser negativo")
    except ValueError:
        print('conserte o erro!')
    else:
        print('a potencia do valor {} é {}'.format(nota, potencia(nota, 2)))
        print('a fatorial do valor {} é {}'.format(nota, factory(nota)))
        print('a divisão do valor {} é {}'.format(nota, dividindo(nota, 4)))
    finally:
        print('agradeço pela sua participação deste sistema!')
validar()

        




              