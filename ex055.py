peso=float(input('Digite o peso da 1º pessoa: '))
maior = peso
menor = peso
for c in range (2,6):
    peso=float(input('Digite o peso da {}º pessoa: '.format(c)))
    if peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print('\033[33mO maior peso é {:.1f} kg e o menor peso é {:.1f} kg\033[m'.format(maior,menor))