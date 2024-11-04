import statistics

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
print('Há {} mulheres com menos de 20 anos'.format(soma))