lista= list
#numeros= list(map(int,input('figite qualquer quantidade de numeros:').split()))
idades= input('digite numeros').split()
numeros=[]
#i= 0 temporario = int(idades[0]) saida = 5
#i= 1 temporario = int(idades[1]) saida = 6
#i = 2 temporario = int(idades[2]) saida = 7
for i in range (0, len(idades) ,1):
  temporario= int(idades[i])
  numeros.append(temporario)
idades=numeros
print(idades)







