sexo=str(input('\033[33mInforme seu sexo [M/F]: \033[m')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo=str(input('\033[36mDados inválidos, informe novamente seu sexo [M/F]: \033[m')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))