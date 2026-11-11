import os

def logo_senai():
    os.system('cls')
    print('='*15)
    print(' SENAI - BAHIA  ')
    print('='*15)

def mostrar_dados(nome, email, telefone):
    print(f'O email {email} e número {telefone} são de {nome}')

logo_senai()
nome = input('Digite seu nome: ')

logo_senai()
email = input('Digite seu email: ')

logo_senai()
telefone = input('Digite seu telefone: ')

logo_senai()
mostrar_dados(nome, email, telefone)
