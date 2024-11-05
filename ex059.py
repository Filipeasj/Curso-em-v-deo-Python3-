opção=4
while opção!=5:
    if opção == 4:
        print('\033[34m-=-=-=-=-=-=-=-=-=-=-\033[m'*2)
        n1=int(input('Primeiro valor: '))
        n2=int(input('Segundo valor: '))
        print('\033[34m-=-=-=-=-=-=-=-=-=-=-\033[m'*2)
    print('\033[34m[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\033[m')
    opção=int(input('\033[36mO que você deseja? '))
    if opção==1:
        resultado=n1+n2
        print('\033[33m{} + {} = {}'.format(n1,n2,resultado))
    elif opção==2:
        resultado=n1*n2
        print('\033[33m{} x {} = {}'.format(n1,n2,resultado))
    elif opção==3:
        if n1>n2:
            print('\033[33mO maior número é {}'.format(n1))
        if n1==n2:
            print('\033[33mOs números são iguais')
        if n2>n1:
            print('\033[33mO menor número é {}'.format(n1))
    elif opção==5:
        print('\033[33mPrograma encerrado')