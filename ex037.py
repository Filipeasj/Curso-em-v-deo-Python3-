n1=int(input('Escolha um número inteiro: '))
print('\033[33m[1] \033[mpara \033[33mbinário')
print('\033[33m[2] \033[mpara \033[33moctal')
print('\033[33m[3] \033[mpara \033[33mhexadeximal')
b=int(input('\033[35mEscolha a base de conversão: '))
if b==1:
    n2=bin(n1)
    base='binário'
    print('\033[32mO número {} em {} será {}\033[m'.format(n1,base,n2[2:]))
elif b==2:
    n2=oct(n1)
    base='octal'
    print('\033[32mO número {} em {} será {}\033[m'.format(n1,base,n2[2:]))
elif b==3:
    n2=hex(n1)
    base='hexadecimal'
    print('\033[32mO número {} em {} será {}\033[m'.format(n1,base,n2[2:]))
else:
    print ('opção inválida')