peso=float(input('\033[34mQual é o seu peso? (Kg) \033[m'))
altura=float(input('\033[34mQual é a sua altura? (m) \033[37m'))
imc= peso/(altura**2)
if imc<18.5:
    print('\033[33mABAIXO DO PESO\033[35m')
elif 18.5<=imc<25:
    print('\033[33mPESO NORMAL\033[35m')
elif 25<=imc<30:
    print('\033[33mSOBREPESO\033[35m')
elif 30<=imc<40:
    print('\033[33mOBESIDADE\033[35m')
elif 40<=imc:
    print('\033[33mOBESIDADE MÓRBIDA\033[35m')