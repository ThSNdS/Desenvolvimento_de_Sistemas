import os
import time
os.system('cls')

login_correto = '123'
senha_correta = 456
tentivas = 0


while True:
    if tentivas == 3:
        print('\nVocê utrapassou e limites de tentativas.')
        time.sleep(5)
        break
    else:
        tentivas += 1
        login = str(input('Digite seu login: '))
        senha = int(input('Escreva sua senha: '))
        if login == login_correto and senha == senha_correta:
            print('Login realizado com sucesso.')
            break
        else:
            print('Login ou senha incorretos.')
            print(f'Você tem {3 - tentivas} chances.')