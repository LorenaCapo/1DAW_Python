# Pràctica 4 - Exercici 09
# Escriu un programa que demani l'amplada i l'alçadad'un triangle i ho dibuixi:

print "Introduce la altura de un triángulo"
altura = input()

print "Introduce la anchura de un triangulo"
anchura = input()

for i in range(altura):
    for j in range(anchura):
        if i==0 or i==altura-1:
            print "*",
        else:
            if j==0 or j==anchura-1:
                print "*",
            else:
                print " ",
    print ""
