print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
total=maisdemil=preçodomaisbarato=cont=0
maisbarato=None
while True:
    opção='A'
    while True:
        nome = str(input('Digite o nome do produto: '))
        if nome.isalpha():
            break
        print('\033[31mValor inválido\033[m')
    while True:
        try:
            preço = float(input('Preço: R$'))
            total +=preço
            if preço > 1000:
                maisdemil+=1
            if cont==0:
                maisbarato=nome
                preçodomaisbarato=preço
            cont+=1
            if preço<preçodomaisbarato:
                preçodomaisbarato=preço
                maisbarato=nome
            break
        except ValueError:
            print('\033[31mValor inválido\033[m')    
    while True:
        opção = str(input('\033[33mQuer continuar? [S/N] \033[m')).strip().upper()
        if opção and opção[0] in 'NS':
            opção=opção[0]
            break
        print('\033[31mValor inválido. Digite S para continuar ou N para sair.\033[m')

    if opção == 'N':
        break
print('-' * 30)
print('''\033[32mO total da compra foi R${:.2f}
Temos {} produto(s) custando mais de R$1000
O produto mais barato foi {} que custa R${:.2f}\033[m'''.format(total,maisdemil,maisbarato,preçodomaisbarato))