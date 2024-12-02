from datetime import date
ano=int(input('\033[33mAno de nascimento: \033[m'))
idade=date.today().year-ano
print('O atleta tem {} anos'.format(idade))
if idade<=9:
    print('\033[34mMirim\033[m')
elif 9<idade<=14:
    print('\033[34mInfantil\033[m')
elif 14<idade<=19:
    print('\033[34mJúnior\033[m')
elif 19<idade<=25:
    print('\033[34mSênior\033[m')
else:
    print('\033[34mMaster\033[m')