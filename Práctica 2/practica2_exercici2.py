#Pràctica 2 - Exercici 2
# Fer un programa que demani a l'usuari dos nombres i que digui quin és el major dels dos.

print "Introduce un número"
num1 = int(raw_input())

print "Introduce otro número"
num2 = int(raw_input())

if num1 > num2:
    print "El primer número introducido es mayor que el segundo."
else:
    print "El segundo número introducido es mayor que el primero."
