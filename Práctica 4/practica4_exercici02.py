#Pr�ctica 4 - Exercici 02
# Escriu un programa que demani dos nombres i escrigui quins nombres son parells
#i quins s�n senars.

print "Introduce un n�mero"
numero1 = input()

print "Introduce un n�mero m�s mayor que " , numero1
numero2 = input()

for x in range (numero1, numero2+1):
    if x%2 == 0:
        print "El n�mero ", x , "es par"
    else:
        print "El n�mero ", x , "es impar"
