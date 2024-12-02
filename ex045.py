from time import sleep
from random import randint
itens=['pedra','papel','tesoura']
pc= randint(0,2)
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador=int(input('Sua jogada: '))
print('\033[33mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\033[m')
sleep(1)
print('-=-'*20)
print('''Computador jogou {}
Jogador jogou {}'''.format(itens[pc],itens[jogador]))
print('-=-'*20)
if pc == 0:
    if jogador == 0:
        print('\033[33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print("\033[31mCOMPUTADOR VENCE\033[m")
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1:
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[33mEMPATE\033[m')
    elif jogador == 2:
        print("\033[32mJOGADOR VENCE\033[m")
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2:
    if jogador == 0:
        print('\033[32mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print("\033[33mEMPATE\033[m")
    else:
        print('JOGADA INVÁLIDA!')

 