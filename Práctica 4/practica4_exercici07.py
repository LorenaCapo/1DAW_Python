# Pr�ctica 4 - Exercici 07
# Escriu un programa que demani l'al�ada d'un triangle i ho dibuixi:

print "Introduce la altura de un tri�ngulo"
altura = input()

for x in range(altura):
    for y in range(x,altura):
            print "*",
    print ""
