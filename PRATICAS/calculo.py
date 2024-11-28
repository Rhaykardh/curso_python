from util.funcoes import Calculadora
def rodar_calculo():
    while 1:
        dados= float(input('digite 1 numero:\n'))
        dados2= float(input( 'digite outro numero:\n'))
        equacao= int(input('digite 1 pra soma, 2 pra subtrair, 3 pra multiplicar ou 4 para dividir os valores e 0 para sair da calculadora:\n'))
        conta= Calculadora()
        if equacao == 1:
            print('a soma de {} e {} dão {}' .format(dados,dados2, conta.soma (dados, dados2) ))
        elif equacao == 2:
            print('a subtração de {} e {} dão {}' .format(dados,dados2, conta.subtracao (dados, dados2) ))     
        elif equacao == 3:
            print('a multiplicação de {} e {} dão {}' .format(dados,dados2, conta.multiplicar (dados, dados2) ))     
        elif equacao == 4:
            print('a divisão de {} e {} dão {}' .format(dados,dados2, conta.dividir ( dados, dados2) ))  
        elif equacao == 0:
            print('você acabou de sair da calculadora! obrigado pela sua participação :)')   
            break   
        else:
            print('opção invalida! tente outra vez...')
    return 0            
rodar_calculo()