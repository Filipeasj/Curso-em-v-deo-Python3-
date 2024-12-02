valor=float(input('Qual o valor da casa? R$'))
salário=float(input('Qual é o valor do seu salário? R$'))
anos=int(input('Quantos anos você pretende pagar? '))
prestação=valor/(anos*12)
if prestação<=salário*0.3:
    print('\033[33mSeu empréstimo foi APROVADO! \033[32ma mensalidade será de R${:.2f} \033[m'.format(prestação))
else:
    print('\033[31mINFELIZMENTE, seu financiamento não será possível! \033[m')