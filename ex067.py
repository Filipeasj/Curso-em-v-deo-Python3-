while True:
    print('-'*40)
    n = int(input('Quer ver a tabuada de qual valor? \033[32m'))
    print('\033[m-'*40)
    if n<0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('\033[33mPROGRAMA TABUADA ENCERRADO. Volte sempre!\033[m')