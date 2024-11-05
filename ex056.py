soma=0
totmulher20=0
maior = 0
homens = 0
for p in range(1,5):
    print('\033[33m----- {} PESSOA-----\033[m'.format(p))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().lower()
    soma = soma + idade
    if p == 1 and sexo == 'm':
        maior = idade
        nomevelho = nome
        homens = homens + 1
    if sexo == 'm' and idade > maior:
        maior = idade
        nomevelho = nome
        homens = homens + 1
    if sexo == 'f' and idade<20:
        totmulher20=totmulher20+1
média = soma/4
print('\033[34mA média do grupo é de {:.0f} anos\033[m'.format(média))
if homens>=1:
    print('\033[33mO homem mais velho tem {} anos e se chama {}\033[m'.format(maior,nomevelho))
else:
    print('\033[33mNão há homens no grupo\033[m')
if totmulher20==0:
    print('\033[36mNão há mulheres com menos de 20 anos no grupo\033[m')
elif totmulher20==1:
    print('\033[36mHá apenas 1 mulher com menos de 20 anos\033[m')
else:
    print('\033[36mAo todo são {} mulheres com menos de 20 anos\033[m'.format(totmulher20))
    
    
#Outro jeito de fazer
'''import statistics
lista = []
nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
velho = nome
idade_velho = idade  # Armazena a idade do primeiro usuário
s = input('Digite o sexo: ')
soma = 0

if s.lower() in ['f', 'feminino']:
    if idade < 20:
        soma += 1
if s.lower() in ['masculino', 'm']:
    lista.append(idade)

for c in range(1, 4):
    n = input('Digite outro nome: ')
    i = int(input('Digite a idade: '))
    s = input('Digite o sexo: ')
    
    lista.append(i)
    if s.lower() in ['masculino', 'm'] and i > idade_velho:
        velho = n
        idade_velho = i  # Atualiza a idade do homem mais velho
    if s.lower() in ['f', 'feminino'] and i < 20:
        soma += 1

if lista:
    print('A média é {}'.format(statistics.mean(lista)))
else:
    print('Nenhuma idade foi registrada.')

print('O homem mais velho é {}'.format(velho))
print('Há {} mulheres com menos de 20 anos'.format(soma))'''