# () indica Tupla (são imutáveis)
#    lanche[1]='batata' NÃO É PERMITIDO
# [] indica Lista
# {} indica Dicionário

lanche = ("hamburguer", "suco", "pizza", "pudim","batata")

#/////////////////////////////////////////////////////

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

for cont in range(0,len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

print(sorted(lanche))
print(lanche)

a=(1,2,4)
b=(5,6,7)
c=a+b
print(c)
print(f'o número 5 aparece na {c.index(5)+1}º posição')