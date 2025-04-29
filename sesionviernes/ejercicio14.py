#Deteccion de un numero par, impar o nulo
numero=int(input("Ingrese un numero entero"))
if numero ==0:
    print("El numero es nulo")
elif numero%2 == 0:
    print("El numero es par")
elif numero%2 !=0:
    print("El numero es impar")
else:
    print("El numero no es entero")    