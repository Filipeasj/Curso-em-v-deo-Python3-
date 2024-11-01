n=int(input('Escolha um número: '))
n2 = 0
for c in range(1,n+1):
    if n%c==0:
        n2+=1
if n2==2:
    print('O número é primo')
else:
    print('O número não é primo')