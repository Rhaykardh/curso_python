def stack():  
    return []
def append(Pilha, carga):
    Pilha.append(carga)
def is_vazia(Pilha):
    if len(Pilha) == 0: 
        return True
    return False
def pop(Pilha):
    if is_vazia(Pilha)== True:
     print('lista vazia')
    return Pilha.pop()
def size(Pilha):
    return len(Pilha)
def acima(Pilha):
    if is_vazia(Pilha)== True:
        print('lista vazia')
    else:
        return Pilha[-1] 
Pilha = stack()
append(Pilha, 10)
print(size(Pilha)== 1)
print(acima(Pilha))
print(pop(Pilha))
