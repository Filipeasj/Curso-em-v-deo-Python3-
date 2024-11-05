from datetime import date
maiores=0
menores=0
for c in range(1,8):
    ano=int(input('\033[32mEm que ano a {}º pessoa nasceu? \033[m'.format(c)))
    if date.today().year-ano>=21:
        maiores=maiores+1
    else:
        menores=menores+1
print('\033[33mHá {} maiores e {} menores\033[m'.format(maiores,menores))