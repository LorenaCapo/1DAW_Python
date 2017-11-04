#Pràctica 4 - Exercici 08
#Escriu un programa que demani l'amplada d'un triangle i ho dibuixi:

print "Introduce la anchura de un triángulo"
anchura = input()

for x in range(anchura-1,-1,-1):
    for y in range(x,anchura,1):
            print "*",
    print ""

for a in range(1,anchura):
    for b in range(a,anchura,1):
            print "*",
    print ""
