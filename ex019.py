from random import choice
p1=input('Primeiro aluno: ')
p2=input('Segundo aluno: ')
p3=input('Terceiro aluno: ')
p4=input('Quarto aluno: ')
lista=[p1,p2,p3,p4]
print('O escolhido é {}'.format(choice(lista)))