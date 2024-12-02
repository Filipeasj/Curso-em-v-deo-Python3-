from datetime import date
print('''\033[34m[m] para masculino
\033[35m[f] para feminino\033[m''')
sexo=str(input('Digite o seu sexo: '))
sexo=sexo.lower()
if sexo == 'f':
    print('\033[33mVocê não precisa se alistar!')
elif sexo =='m':
    ano=int(input('Insira o ano em que você nasceu: '))
    idade=date.today().year-ano
    print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,date.today().year))
    if idade<18:
        tempo=18-idade
        print('\033[32mDaqui a {} ano(s) você deverá se alistar\033[m'.format(tempo))
        print('\033[33mSeu alistamento será em {}\033[m'.format(date.today().year+tempo))
    elif idade == 18:
        print('\033[33mVocê tem que se alistar IMEDIATAMENTE!\033[m')
    elif idade>18:
        tempo=idade-18
        print('\033[31mvocê deveria ter se alistado há {} ano(s)\033[m'.format(tempo))
        print('\033[33mSeu alistamento foi em {}\033[m'.format(date.today().year-tempo))
else:
    print('valor inválido!')