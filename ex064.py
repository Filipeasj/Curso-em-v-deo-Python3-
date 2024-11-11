n= cont = soma = 0
while n!=999:
    n=int(input('Digite um valor (999 PARA PARAR A SOMA): '))
    if n!=999:
        cont=cont+1
        soma=soma+n
print('\033[33mVocê digitou {} números e a soma deles é igual a {}\033[m'.format(cont,soma))