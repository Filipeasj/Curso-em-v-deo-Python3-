seta='\u2192'
print('-=-'*10)
n=int(input('Primeiro termo: '))
r=int(input('Razão da PA: '))
cont=10
print('\033[33mOs dez primeiros termos dessa PA são:\033[m')
while cont!=0:
    print('{}{} '.format(n,seta),end='')
    n=n+r
    cont=cont-1
print('\033[m FIM!')