v=float(input('Qual é a velocidade do carro: '))
if v>80:
    multa=(v-80)*7
    print('MULTADO! Você foi multado no valor de {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com cuidado!')