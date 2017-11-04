#Pràctica 4 - Exercici 03
#Escriu un programa que demani 2 nombres i escrigui la suma de sencers des
# del primer nombre fins al segon.

print "Introduce un número"
numero1 = input()

print "Introduce un número mayor que " , numero1
numero2 = input()

contador = 0
for i in range(numero1, numero2+1):
    contador = contador + i
print "La suma desde " , numero1 , " hasta " , numero2 , " es " , contador
