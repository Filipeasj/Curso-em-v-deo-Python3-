print('-=-'*10)
print('ANALISADOR DE TRIâNGULOS')
print('-=-'*10)
a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if b+c>a and b+a>c and c+a>b:
    print('É POSSÍVEL formar um triângulo')
else:
    print('NÃO É POSSÍVEL formar um triângulo')