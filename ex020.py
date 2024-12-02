from random import shuffle
p1=input('Digite o nome do primeiro: ')
p2=input('Digite o nome do segundo: ')
p3=input('Digite o nome do terceiro: ')
p4=input('Digite o nome do quarto: ')
lista=[p1,p2,p3,p4]
shuffle(lista)
print('A ordem é: {}'.format(lista))