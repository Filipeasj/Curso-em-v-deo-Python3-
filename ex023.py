num=int(input('Informe um número: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade : {}'.format(u))
print('Dezena : {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#n=input('Digite um número: ')
#print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(n[3],n[2],n[1],n[0]))