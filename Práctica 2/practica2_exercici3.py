#Pràctica 2 - Exercici 3
# Exercici que demani a l'usuari l'espai recorregut per un cotxe (en km) i el
# temps que ha tardat (en hores) i que calculi a quina velocitat anava.

print "¿Cuánto kilómetros has recorrido?"
km = int(raw_input())

print "¿Cuánto tiempo has tardado?"
tiempo = int(raw_input())

recorrido = km / tiempo
print "Has recorrido ", recorrido
