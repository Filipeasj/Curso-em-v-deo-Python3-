seta_direita = "\u2192"
print('='*30)
print('      10 TERMOS DE UM PA')
print('='*30)
primeiro=int(input('Primeiro termo: '))
razão=int(input('Razão: '))
for c in range(primeiro,primeiro+10*razão, razão):
    print(c, seta_direita, end=' ')
print('Acabou')