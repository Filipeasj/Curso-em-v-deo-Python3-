print('-=-'*10)
print('ANALISADOR DE TRIâNGULOS')
print('-=-'*10)
a=float(input('\033[034mPrimeiro segmento: \033[m'))
b=float(input('\033[034mSegundo segmento: \033[m'))
c=float(input('\033[034mTerceiro segmento: \033[m'))
if b+c>a and b+a>c and c+a>b:
    if a==b==c:
        print('\033[33mEQUILÁTERO\033[m')
    elif a==b or a==c or b==c:
        print('\033[33mISÓSCELES\033[m')
    elif a!=b!=c and a!=c:
        print('\033[33mESCALENO\033[m')
else:
    print('\033[31mNÃO É POSSÍVEL formar um triângulo\033[m')