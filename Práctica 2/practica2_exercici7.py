#Pr�ctica 2 - Exercici 7
# Fer un programa que demani un nombre de nom�s 3 xifres a un usuari.
# Si l'usuari entra un nombre que no sigui de 3 xifres ha de donar error.

numero = int(raw_input("Introduce una cifra "))

if (numero >=100) & (numero <=999):
    print numero
else:
    print "El n�mero introducido no tiene 3 cifras"
