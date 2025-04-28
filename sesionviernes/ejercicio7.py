lado1= int(input("Ingrese el lado 1 del triángulo: "))
lado2= int(input("Ingrese el lado 2 del triángulo: "))
lado3= int(input("Ingrese el lado 3 del triángulo: "))

if lado1== lado2 and lado1==lado3:      
    print("Es un triángulo equilátero")
elif lado1== lado2 or lado1==lado3 or lado2==lado3:
    print("Es un triángulo isósceles")
elif lado1!= lado2 and lado1!=lado3 and lado2!=lado3:
    print("Es un triángulo escaleno")
else:
    print("error")