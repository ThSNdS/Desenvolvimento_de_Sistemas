import os
os.system("cls")

idad = int(input('Digite sua idade: '))
sexo = input('Digite o sexo (M ou F): ').upper()

if idad >= 18 and sexo == 'M':
    resultado = "Deve apresentar-se ao serviço militar."
else:
    resultado = "Não deve apresentar-se ao serviço militar."

print (resultado)