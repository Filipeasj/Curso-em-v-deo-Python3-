import emoji
from time import sleep
for c in range (10,-1,-1):
    print(c)
    sleep(1)
print(emoji.emojize(':cone_de_festa:'*10,language='pt'))
print('\033[32mBUM! BUM! POOW!\033[m')