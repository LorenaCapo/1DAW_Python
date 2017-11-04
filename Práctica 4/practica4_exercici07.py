# Pràctica 4 - Exercici 07
# Escriu un programa que demani l'alçada d'un triangle i ho dibuixi:

print "Introduce la altura de un triángulo"
altura = input()

for x in range(altura):
    for y in range(x,altura):
            print "*",
    print ""
