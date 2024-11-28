Dados= input('digite qualquer quantidade de numeros separados por espaço')
lista_dados= Dados.split()
numeros_dados= map(int,lista_dados)
lista_numeros= list(numeros_dados)
soma_notas= 0
for i in lista_numeros:
    soma_notas += i
media= soma_notas/len(lista_numeros)
print(media)
