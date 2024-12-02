from random import randint 

cont = 0
print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)

while True:
    jogada = 'a'
    while True:
        try:
            v = int(input('Diga um valor: '))
            break
        except ValueError:
            print('\033[31mInsira apenas um valor numérico\033[m') 
    
    while jogada not in 'PI' or jogada=='':
        jogada = str(input('Par ou ímpar? [P/I]: ')).strip().upper()
        if jogada not in 'PI' or jogada=='':
            print('\033[31mValor inválido. Digite P para para par ou I para ímpar\033[m')
    
    computador = randint(0, 10)
    total = v + computador
    resultado = 'PAR' if total % 2 == 0 else 'IMPAR'
    
    print('=-' * 30)
    print(f'Você jogou {v} e o computador {computador}. Total de {total} DEU {resultado}')
    
    if jogada[0] == resultado[0]:
        print('\033[32mVocê VENCEU!\033[m')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print('\033[31mVocê PERDEU!\033[m')
        print('=-' * 30)
        break

print(f'\033[33mGAME OVER! Você venceu {cont} vez(es).\033[m')
