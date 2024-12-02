n1=float(input('Insira a primeira nota: '))
n2=float(input('Insira a segunda nota: '))
lista=[n1,n2]
media=sum(lista)/len(lista)
if media<5:
    print('\033[31mREPROVADO! média = {:.1f}\033[m'.format(media))
elif 5<=media<=6.9:
    print('\033[33mRECUPERAÇÃO! média = {:.1f}\033[m'.format(media))
elif media>=7:
    print('\033[32mAPROVADO! média = {:.1f}\033[m'.format(media))