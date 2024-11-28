class Dicionario: 
    def __init__(self, conteudo=None):
        if conteudo == None:
            self.Dados= dict()
        else:
            self.Dados= dict(conteudo)
    def adicionar(self, informacao):
        self.Dados[informacao[0]] = informacao[1]
    def __str__(self):
        return str(self.Dados)
    def size(self):
        return len(self.Dados)
    def delete(self, informacao):
        if informacao in self.Dados:
            return self.Dados.pop(informacao)
        else:
            raise KeyError('o codigo falhou por que {} n existe'.format(informacao))
    def peek(self, informacao):
        return self.Dados.get(informacao, KeyError('falha no codigo'))
final= Dicionario()  
print(final)

final.adicionar(informacao=[4, 7])
print(final)

print(final.size())

final.delete(informacao= 4)
print(final)

print (final.peek(4))

        
       

    

    