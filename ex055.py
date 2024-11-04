peso=float(input('Digite o peso da pessoa 1 = '))
a = peso
b = peso
for c in range (2,6):
    peso=float(input('Digite o peso da pessoa {} = '.format(c)))
    if peso>a:
        a=peso
    elif peso<b:
        b=peso
print('\033[33mO maior peso é {:.2f} kg e o menor peso é {:.2f} kg\033[m'.format(a,b))