def gerador_infinito():
    n= 0
    while True:
        yield n
        n += 1

gen = gerador_infinito()       
for  i in range (10):
    print (next(gen))
aula= int(input('digite o tamanho do laço'))
for i in range(10, aula,): 
    print(next(gen))
    print ('i' ,i)