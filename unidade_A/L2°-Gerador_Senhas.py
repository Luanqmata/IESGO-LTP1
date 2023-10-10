import random
import time
def gerador_senha():
    digito= random.randint(0,9)
    digito1 = random.randint(0,9)
    digito2 = random.randint(0,9)
    digito3 = random.randint(0,9)
    digito4 = random.randint(0,9)
    digito5 = random.randint(0,9)
    digito6 = random.randint(0,9)
    digito7 = random.randint(0,9)
    digito8 = random.randint(0,9)
    digito9 = random.randint(0,9)
    digito10 = random.randint(0,9)
    
    qnt_numeros_user = int(input('quantos Numerais sua senha deve ter?'))
    
    print('Gerando senha.')
    time.sleep(1)
    print('Gerando senha..')
    time.sleep(1.5)
    print('Gerando senha...')
    time.sleep(2)
    
    if qnt_numeros_user == 1:
        print('Sua senha é :' , digito)
    elif qnt_numeros_user == 2:
        print('Sua senha é :' , digito,digito1)
    elif qnt_numeros_user == 3:
        print('Sua senha é :' , digito,digito1,digito2,digito3)
    elif qnt_numeros_user == 4:
        print('Sua senha é :' , digito,digito1,digito2,digito3,digito4)
    elif qnt_numeros_user == 5:
        print('Sua senha é :' , digito,digito1,digito2,digito3,digito4,digito5)
    elif qnt_numeros_user == 6:
        print('Sua senha é :' , digito,digito1,digito2,digito3,digito4,digito5,digito6)
    elif qnt_numeros_user == 7:
        print('Sua senha é :' , digito,digito1,digito2,digito3,digito4,digito5,digito6,digito7)
    elif qnt_numeros_user == 8:
        print('Sua senha é :' , digito,digito1,digito2,digito3,digito4,digito5,digito6,digito7,digito8)
    elif qnt_numeros_user == 9:
        print('Sua senha é :' , digito,digito1,digito2,digito3,digito4,digito5,digito6,digito7,digito8,digito9)
    elif qnt_numeros_user == 10:
        print('Sua senha é :' , digito,digito1,digito2,digito3,digito4,digito5,digito6,digito7,digito8,digito9,digito10)
    else:
        print('Infelizmente esse gerador só geras 10 digitos para senhas.')
print(gerador_senha())
    
