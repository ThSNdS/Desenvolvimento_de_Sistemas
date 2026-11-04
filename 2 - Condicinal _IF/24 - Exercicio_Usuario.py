import os
os.system("cls")

print('Conclua o login')
usua = str(input('Escreva seu Usuário: '))
senh = (input('Digite sua senha: '))

if usua == 'Senai' and senh == 123456:
    print('Bem-vindo')
else:
    print('Login ou senha inválidos')
