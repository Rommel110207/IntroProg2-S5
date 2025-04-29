#Verificacion de un dia laboral
idia=int(input("Ingrese el dia de la semana (1-7)"))
if idia == 1 or idia == 2 or idia == 3 or idia == 4 or idia == 5:
    print("Es un dia laboral") 
elif idia == 6 or idia == 7:
    print("No es un dia laboral")
else:
    print("Dia no valido")