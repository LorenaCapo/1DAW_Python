# Pràctica 4 - Exercici 04
# Escriu un programa que demani un nombre i calculi el seu factorial

print "Introduce un número para calcular su factorial"
numero = input()

cont = 1
for i in range(cont, numero+1):
    cont = cont * i

print "El factorial del número " , numero , " es " , cont
