#Comparacion de 3 números
num1= int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))
num3= int(input("Ingrese el tercer número: "))

if num1>num2 and num1>num3:
    print(f"El número mayor es: {num1}")
elif num2>num1 and num2>num3:
    print(f"El número mayor es: {num2}")
elif num3>num1 and num3>num2:
    print(f"El número mayor es: {num3}")
elif num1==num2 and num1>num3:
    print(f"El número mayor es: {num1} y {num2}")
elif num1==num3 and num1>num2:
    print(f"El número mayor es: {num1} y {num3}")
elif num2==num3 and num2>num1:
    print(f"El número mayor es: {num2} y {num3}")
elif num1==num2 and num2==num3:
    print(f"Los números son iguales: {num1}, {num2} y {num3}")
else:
    print("Error")