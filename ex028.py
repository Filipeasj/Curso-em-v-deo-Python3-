from random import randint
from time import sleep
c=randint(0,5)
print('-=-'*10)
print('\033[33m Vou pensar em um número entre 0 e 5...\033[37m')
print('-=-'*10)
p=int(input('Em que número pensei? '))
print('\033[33mPROCESSANDO...\033[37m')
sleep(3)
if p==c:
    print('\033[32m PARABÉNS! você ganhou! eu realmente pensei em {}\033[37m'.format(c))
else:
    print('\033[31m GANHEI! o número era {} e não {}\033[37m'.format(c,p))