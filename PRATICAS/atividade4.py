n1= int(input('digite um numero'))
n2= int(input('digite um numero'))
n3= int(input('digite um numero'))
if n1 > n2 and n1> n3:
    print(n1, 'o primeiro é o maior numero')
elif n2 > n3 and n2> n1:
    print(n2, 'o segundo é o maior numero')
else:
    print(n3, 'o terceiro é o maior numero')
