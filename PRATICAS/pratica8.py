class Fila:
    def __init__(self, elementos_lista = []):
        self.valor= elementos_lista
    def enqueue(self, aula, aula2):
        self.valor.append(aula)
        self.valor.append(aula2)
    def denqueue(self):
       return self.valor.pop(1) 
total= Fila([6, 9])    
total.enqueue(6, 9)
print(total.valor)
            
        