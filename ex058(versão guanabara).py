from random import randint
computador=randint(0,10)
print('\033[36mSou seu computador...')
print('\033[33mAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? \033[m')
jogador=None
cont=0
while jogador!=computador:
    jogador=int(input('Qual é seu palpite? '))
    cont=cont+1
    if jogador>computador:
        print('Menos... Tente mais uma vez')
    elif jogador<computador:
        print('Mais... Tente mais uma vez')
print('\033[32mAcertou com {} tentativas. Parabéns!\033[m'.format(cont))