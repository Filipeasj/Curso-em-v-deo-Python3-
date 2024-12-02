maiores = homens = mulheres = 0

while True:
    opção=None
    while True:
        try:
            idade = int(input('Idade: '))
            if idade > 18:
                maiores +=1
            break
        except ValueError:
            print('\033[31mvalor inválido. Tente de novo!\033[m')

    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo in 'MF' and sexo:
            if sexo == 'M':
                homens +=1
            elif sexo == 'F' and idade < 20:
                mulheres +=1
            break
        print('\033[31mSexo inválido. Digite M para masculino ou F para feminino.\033[m')

    while True:
        opção = input('\033[33mQuer continuar? [S/N] \033[m').strip().upper()
        if opção == 'S' or opção=='N':
            break
        print('\033[31mInsira um valor válido ("S" ou "N").\033[m')
    
    if opção == 'N':
        break
print('-----FIM DO PROGRAMA-----')
print(f'\033[35mO total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homem(s) cadastrados')
print(f'E temos {mulheres} mulher(es) com menos de 20 anos\033[m')