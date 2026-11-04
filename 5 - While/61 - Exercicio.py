import os
import time
os.system('cls')

login_correto = 'admin123'
senha_correta = 123456

while True:
    login = input('Digite seu login: ')
    senha = int(input('Escreva sua senha: '))
    if login == login_correto and senha == senha_correta:
        print('Login realizado com sucesso.')
        break
    else:
        print('Login ou senha incorretos.')
        time.sleep(2)
        os.system('cls')