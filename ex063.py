seta='\u2192'
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n=int(input('\033[33mQuantidade de elementos Fibonacci: \033[m'))
n1=0
n2=1
n=n-2
print(n1,seta,n2,seta,end=' ')
while n!=0:
    n3=n1+n2
    print(n3,seta,end=' ')
    n1=n2
    n2=n3
    n=n-1
print('ACABOU!')