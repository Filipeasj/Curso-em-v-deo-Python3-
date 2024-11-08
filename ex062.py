seta='\u2192'
print('-=-'*10)
termo=int(input('Primeiro termo: '))
r=int(input('Razão: '))
cont=1
total = 0
mais = 10
print('Os dez primeiros termos dessa PA são:')
while mais!=0:
    total=total+mais
    while cont <= total:
        print('\033[33m{} {} \033[m'.format(termo, seta),end='')
        termo=termo+r
        cont=cont+1
    print('PAUSA')
    mais=int(input('Quantos termos a mais você mais deseja? '))
print('\033[32mProgressão com {} termos finalizada com sucesso\033[m'.format(total))