wage = float(input('Digite o valor do seu salário: R$'))
if wage>1250:
    print('O novo salário será de R${:.2f} agora'.format(wage*1.1))
else:
    print('O novo salário será de R${:.2f} agora'.format(wage*1.15))