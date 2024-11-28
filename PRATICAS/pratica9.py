class Conjunto:
    def __init__(self, conjunto1= [1, 2, 3], conjunto2=[6,4,5]):
        self.valor= None
        self.conjunto1= set(conjunto1)
        self.conjunto2= set(conjunto2)
    def getConjunto1(self):
        return self.conjunto1
    def setConjunto1(self, conjunto1):
        self.conjunto1= conjunto1
    def uniao(self):
        self.valor= self.conjunto2.union(self.conjunto1)
        return self.valor 
finalizar= Conjunto()
print (finalizar.uniao())
