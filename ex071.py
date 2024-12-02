print('='*40)
print('BANCO ALVES')
print('='*40)
while True:
    try:
        saque=int(input('Qual será o valor sacado? R$'))
        break
    except ValueError:
        print("\033[31mvalor inválido\033[m")
total = saque
céd=100
totcéd=0
while True:
    if total >= céd:
        total -=céd
        totcéd +=1
    else:
        if totcéd>0:
            print(f'\033[33mTotal de {totcéd} cédula(s) de R${céd}\033[m')
        if céd==100:
            céd=50
        elif céd==50:
            céd=20
        elif céd ==20:
            céd=10
        elif céd==10:
            céd=1
        totcéd=0
        if total == 0:
            break
print('='*40)
print('Volte sempre ao BANCO ALVES! Tenha um bom dia!')