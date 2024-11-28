class No:
    def __init__(self, dado):
        self.dado= dado
        self.prox= None
class Encadeamento:
    def __init__(self):
        self.ancora= None
    def inserir(self, dado):
        novo_no= No(dado)
        if self.ancora == None:
            self.ancora= novo_no
            return self.ancora.dado
        else:
            valor= self.ancora
            while valor.prox:
                valor = valor.prox
            valor.prox = novo_no
            return valor.prox.dado
    def pecorrer(self):
        resultado= self.ancora
        while resultado:
            print(resultado.dado, end=">")
            resultado= resultado.prox
        print('acabou')
    def delete(self, retirar):
        tirar= self.ancora
        if tirar and tirar.dado == retirar:
            self.ancora = tirar.prox 
            tirar = None
            return tirar
        anterior= None
        while tirar and tirar.dado != retirar:
            anterior= tirar
            tirar= tirar.prox
        if tirar == None:
            return None
        else:
            anterior.prox = tirar.prox
            tirar = None

finalizar= Encadeamento()
print(finalizar.inserir(3))
print(finalizar.inserir(4))
finalizar.pecorrer()
finalizar.delete(3)
finalizar.pecorrer()

