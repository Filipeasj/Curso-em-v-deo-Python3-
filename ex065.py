soma = cont = maior = menor = 0
opção = 'S'
while opção in 'Ss':
    while True:
        try:
            n = int(input('Digite um valor: '))
            break 
        except ValueError:
            print('\033[31mValor inválido! Por favor, digite um número inteiro.\033[m')
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    while True:
        opção = input('\033[36mVocê ainda deseja mais valores [S/N]? \033[m').strip().upper()
        if opção in 'SN':
            break
        else:
            print('\033[31mValor inválido! Por favor, digite "S" para sim ou "N" para não.\033[m')
if cont > 0:
    media = soma / cont
    print(f'\033[33mVocê digitou {cont} números e a média é {media:.2f}\033[m')
    print(f'\033[33mO maior valor é {maior}\033[m')
    print(f'\033[33mO menor valor é {menor}\033[m')
else:
    print('\033[33mNenhum valor válido foi digitado.\033[m')