from random import randint
seta_direita = "\u2192"
print('\033[33m-=-=-=-=-=-=-\033'*5)
print('\033[3mVou pensar em um número entre 0 e 10. Tente advinhar...')
print('\033[33m-=-=-=-=-=-=-\033[m'*5)
lista = [0,1,2,3,4,5,6,7,8,9,10]
jogador = 17
computador = None
tentativas = 0
while jogador != computador:
    computador = randint(0,10)
    print('Em que número pensei?')
    print(seta_direita, end=' ')
    jogador=int(input('Jogador: '))
    if jogador == computador:
        print('\033[32mVocê Venceu! Eu também pensei em {}'.format(computador))
    else:
        print('\033[31mVocê Perdeu! Eu pensei em {}\033[m'.format(computador))
        print('\033[33mTente de novo!\033[m')
        tentativas += 1
print('* (Você precisou de {} palpites para vencer)\033[m'.format(tentativas))