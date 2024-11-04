frase=str(input('Digite uma frase: ')).strip().lower()
frase=str(frase.replace(' ',''))
frase2=str('')
for c in range(len(frase)-1,-1,-1):
   frase2=frase2+frase[c]
if frase2==frase:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
    
#JEITO MAIS FÁCIL (SEM ESTRUTURA FOR)
'''frase=str(input('Digite uma frase:')).strip()
frase=frase.replace(' ','')
frase_invertida = frase[::-1]
if frase_invertida==frase:
    print('é um palíndromo')
else:
    print('não é um palíndromo')'''