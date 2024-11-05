frase=str(input('Digite uma frase: ')).strip().upper()
frase=str(frase.replace(' ',''))
frase2=str('')
for c in range(len(frase)-1,-1,-1):
   frase2=frase2+frase[c]
print('O inverso de {} é {}'.format(frase,frase2))
if frase2==frase:
    print('\033[33mÉ um palíndromo\033[m')
else:
    print('\033[31mNão é um palíndromo\033[m')
    
#JEITO MAIS FÁCIL (SEM ESTRUTURA FOR)
'''frase=str(input('Digite uma frase:')).strip()
frase=frase.replace(' ','')
frase_invertida = frase[::-1]
if frase_invertida==frase:
    print('\033[33mé um palíndromo\033[m')
else:
    print('\033[33mnão é um palíndromo\033[m')'''