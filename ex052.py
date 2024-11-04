n=int(input('Escolha um número: \033[32m'))
divísivel=0
for c in range (1,n+1):
    if n%c==0:
        print('\033[33m',c,'\033[m', end='')
        divísivel+=1
    else:
        print('\033[31m',c,'\033[m',end='')
print('\nO número {} foi divísivel {} vezes'.format(n, divísivel))
if divísivel==2:
    print('Logo, O número é primo!')
else:
    print('Logo, o número NÃO é primo!')