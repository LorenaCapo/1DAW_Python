#Pr�ctica 2 - Exercici 6
# Fer un programa que demani un nombre de com a m�xim 3 xifres a un usuari
# Si l'usuari entra un nombre de m�s de 3 xifres ha de donar un error.

numero = int(raw_input("Introduce una cifra "))

if (numero >=0) & (numero <=999):
    print numero
else:
    print "El n�mero introducido no tiene como m�ximo 3 cifras"
