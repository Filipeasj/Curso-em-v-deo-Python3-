n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
opção=0
while opção!=5:
    print('\033[33m[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\033[m')
    opção=int(input('\033[36m>>> O que você deseja? \033[m'))

    if opção==1:
        soma=n1+n2
        print('{} + {} = {}'.format(n1,n2,soma))
    elif opção==2:
        produto=n1*n2
        print('{} x {} = {}'.format(n1,n2,produto))
    elif opção==3:
        if n1>n2:
            print('Entre {} e {} o maior número é {}'.format(n1,n2,n1))
        if n1==n2:
            print('Os números são iguais')
        if n2>n1:
            print('Entre {} e {} o maior número é {}'.format(n1,n2,n2))
    elif opção==4:
        n1=int(input('Primeiro valor: '))
        n2=int(input('Segundo valor: '))
    elif opção==5:
        print('finalizando')
    else:
        print('valor inválido')
    print('-=-=-=-'*10)
print('Programa encerrado! Volte sempre!')