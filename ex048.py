soma = 0
contador = 0
for c in range (1,501,2):
    if c%3==0:
        soma = soma + c
        contador=contador+1
print('\033[33mA soma de todos os {} valores solicitados é {}\033[m'.format(contador,soma))