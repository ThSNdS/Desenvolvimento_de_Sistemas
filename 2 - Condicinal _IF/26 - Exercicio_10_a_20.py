import os
os.system("cls")

nume = int(input('Digite um número: '))

minimo = 10 
maximo = 20
ante = nume - minimo
succ = maximo - nume 

if nume > minimo and nume < maximo:
    print(F'!Acertou Parabéns!.\nO seu número estar {ante} casas do {minimo} e {succ} do {maximo}')