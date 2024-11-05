sexo=None
while sexo!='M' and sexo!='F':    
    sexo=str(input('\033[34mInsira o sexo [M/F]: \033[m'))
    if sexo!='M' and sexo!='F':
        print('\033[33mvalor inválido! Tente de novo!\033[m')
print('\033[32mAcabou\033[m')