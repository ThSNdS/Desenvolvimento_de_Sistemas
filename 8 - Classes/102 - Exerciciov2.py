from dataclasses import dataclass
import os
os.system('cls')

# CRIE UMA CLASSE PARA OS DADOS DE UM CLIENTE.
# DADOS: NOME, TELEFONE E E-MAIL.
@dataclass
class cliente:
    nome: str
    telefone: int
    e_mail: str
    # Função dentro da classe.
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'E-Mail: {self.e_mail}')
        print('='*30)
        # Função somente para enviar e-mails.
    def email_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'E-Mail: {self.e_mail}')
        print('='*30)
        # Função somente para enviar whatsapp.
    def whatsapp_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print('='*30)

lista_clientes = []
for i in range(2):
    dados = cliente(
        nome= input('Digite seu nome: '),
        telefone= int(input('Digite seu número de telefone: ')),
        e_mail= input('Digite seu e-mail: ')
    )
    lista_clientes.append(dados)

print('\nExibindo Dados')
for cliente in lista_clientes:
    cliente.mostrar_dados()
print('\n Exibindo Dados')
for cliente in lista_clientes:
    cliente.email_marketing()
print('\n Exibindo Dados')
for cliente in lista_clientes:
    cliente.whatsapp_marketing()