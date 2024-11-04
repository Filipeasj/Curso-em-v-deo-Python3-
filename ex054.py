from datetime import date
maiores=0
menores=0
for c in range(1,8):
    ano=int(input('Digite o ano de nascimento da pessoa {} = '.format(c)))
    if date.today().year-ano>=21:
        maiores=maiores+1
    else:
        menores=menores+1
print('Há {} maiores e {} menores'.format(maiores,menores))