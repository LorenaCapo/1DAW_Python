#Pràctica 4 - Exercici 02
# Escriu un programa que demani dos nombres i escrigui quins nombres son parells
#i quins són senars.

print "Introduce un número"
numero1 = input()

print "Introduce un número más mayor que " , numero1
numero2 = input()

for x in range (numero1, numero2+1):
    if x%2 == 0:
        print "El número ", x , "es par"
    else:
        print "El número ", x , "es impar"
