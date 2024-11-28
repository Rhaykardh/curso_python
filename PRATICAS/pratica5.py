def potencia(valor, numero):
    return valor**numero

#print(potencia(valor[0], valor[1]))

def finalizar(valor): 
    aula= []
    for ramon in valor:
        atividade= potencia(ramon, 2)
        aula.append(atividade)
    return aula  
valor= list(map(int,input('digite 2 numeros').split()))
valor.sort()  
print(finalizar(valor))

    

