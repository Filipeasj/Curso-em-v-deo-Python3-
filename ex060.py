n=int(input('\033[34mDigite um número: \033[m'))
f=1
print('\033[33mCalculando {}! = '.format(n),end='')
while n>0:
    print('{}'.format(n),end='')
    print(' x ' if n > 1 else ' = ',end='')
    f=f*n
    n=n-1
print('{}\033[m'.format(f))




# Utilizando estrutura for
'''n=int(input('\033[34mDigite um número: \033[m'))
n2=n-1
print('\033[33m{}! = {}'.format(n,n),end='')
for c in range (n,1,-1):
    n=n*n2
    print(' x {}'.format(n2),end='')
    n2=n2-1
print(' = {}\033[m'.format(n))'''