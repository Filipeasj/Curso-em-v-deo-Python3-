frase=str(input('Digite uma frase:')).strip()
frase=frase.replace(' ','')
frase_invertida = frase[::-1]
if frase_invertida==frase:
    print('é um palíndromo')
else:
    print('não é um palíndromo')