from datetime import date
year=int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if year==0:
    year=date.today().year
if ((year%4==0) & (year%100!=0)) or ((year%100==0) & (year%400==0)):
    print(year,'é um ano bissexto')
else:
    print(year,'não é um ano bissexto')