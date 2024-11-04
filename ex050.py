soma = 0
cont = 0
for c in range (1,7):
    n=int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        cont=cont+1
        soma = soma +n
if cont==1:
            print('\033[33mVocê informou {} número PAR e o seu valor é {}\033[m'.format(cont, soma))
elif cont==0:
        print('\033[33mVocê não informou nenhum número PAR\033[m')
else:print('\033[33mVocê informou {} números PARES e a soma deles é {}\033[m'.format(cont, soma))