# Pr�ctica 4 - Exercici 04
# Escriu un programa que demani un nombre i calculi el seu factorial

print "Introduce un n�mero para calcular su factorial"
numero = input()

cont = 1
for i in range(cont, numero+1):
    cont = cont * i

print "El factorial del n�mero " , numero , " es " , cont
