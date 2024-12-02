d=float(input('Qual é a distância da viagem: '))
preço= d * 0.50 if d<=200 else d*0.45
print('E o preço de sua passagem será de {:.2f}'.format(preço))