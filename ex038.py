n1=int(input('Escolha um número: '))
n2=int(input('Escolha outro número: '))
if n1>n2:
    print('\033[33m{} é maior do que {}\033[m'.format(n1,n2))
elif n2>n1:
    print('\033[33m{} é maior do que {}\033[m'.format(n2,n1))
else:
    print('\033[36mNÃO existe valor maior, pois os dois são iguais!\033[m')
