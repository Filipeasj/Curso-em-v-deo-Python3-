
print('{:=^40}'.format(' LOJAS ALVES '))
preço=float(input('Preço das compras: R$'))
print('\033[34m[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão\033[m')
c=int(input('Escolha o modo de pagamento: '))
if c==1:
    print('\033[33mvalor final= R${:.2f}\033[m'.format(preço*0.9))
elif c==2:
    print('\033[33mvalor final = R${:.2f}\033[m'.format(preço*0.95))
elif c==3:
    print('\033[33mvalor final = R${:.2f}\033[m'.format(preço))
    print('\033[32m2 prestações de R${:.2f}\033[m'.format(preço/2))
elif c==4:
    parcelas=int(input('Quantas parcelas: '))
    print('\033[33mvalor final = R${:.2f}\033[m'.format(preço*1.2))
    print('\033[32m{} prestações de R${:.2f}\033[m'.format(parcelas,(preço*1.2)/parcelas))
else:
    print('\033[31mOPÇÃO INVÁLIDA! TENTE NOVAMENTE!')