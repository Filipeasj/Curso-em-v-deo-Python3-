FirstTerm=int(input('Escolha o primneiro termo: '))
reason=int(input('Escolha a razão da P.A: '))
for c in range(0,10):
    value=FirstTerm+reason*c
    print('a{} = {}' .format(c+1,value))