from math import sin,cos,tan, radians
a=float(input('Escreva um ângulo: '))
s=sin(radians(a))
c=cos(radians(a))
t=tan(radians(a))
print('Sobre o número {}\nseno = {:.2f}\ncosseno = {:.2f}\ntangente = {:.2f}'.format(a,s,c,t))