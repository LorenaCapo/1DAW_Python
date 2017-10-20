#Pràctica 2 - Exercici 5
# Escriure un programa on el usuari entri 3 qualificacions d'exàmens i calculi
# la mitja d'aquestes qualificacions.

nota1 = int(raw_input("Introduce tu primera nota"))
nota2 = int(raw_input("Introduce tu segunda nota"))
nota3 = int(raw_input("Introduce tu tercera nota"))

notaFinal = (nota1 + nota2 + nota3) / 3
print "La media de tus calificaciones es ", notaFinal
