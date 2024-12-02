a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
c=int(input('Digite o terceiro número:'))
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('-=-'*10)
print('O menor é {}'.format(menor))
print('O maior é {}'.format(maior))




# economizou tudo isso:
"""if n1>n2:
    if n1>n3:
        print('O maior é {}'.format(n1))
    else:
        print('O maior é {}'.format(n3))
else:
    if n2>n3:
        print('O maior valor é {}'.format(n2))
    else:
        print('O maior é {}'.format(n3))
if n1<n2:
    if n1<n3:
        print('O menor é {}'.format(n1))
    else:
        print('O menor número é {}'.format(n3))
else:
    if n2<n3:
        print('O menor é {}'.format(n2))
    else:
        print('O menor número é {}'.format(n3))"""