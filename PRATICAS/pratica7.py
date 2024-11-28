Fila= []
def size(Fila):
    return len(Fila)
def is_empty(Fila):
    return size(Fila)== 0
def enqueue(Fila, Ramon):
     Fila.append(Ramon)
def denqueue(Fila):
    if is_empty(Fila):
         raise IndexError('não há elementos na lista')
    else:
        return Fila.pop(0)



def peek(Fila):
    if is_empty(Fila):
         raise IndexError('não há elementos na lista')
    else:
        return Fila[0]

enqueue(Fila, 8)

vazio= is_empty(Fila)

denqueue(Fila)

tamanho= size(Fila)

enqueue(Fila, 1 )
print(type (Fila))
print(peek(Fila))
print(Fila)
