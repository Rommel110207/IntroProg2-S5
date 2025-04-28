def menu():
    print("Menú de Operaciones Básicas")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "5":
        print("Saliendo del programa...")
        break

    if opcion in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == "1":
                print("Resultado:", suma(num1, num2))
            elif opcion == "2":
                print("Resultado:", resta(num1, num2))
            elif opcion == "3":
                print("Resultado:", multiplicacion(num1, num2))
            elif opcion == "4":
                print("Resultado:", division(num1, num2))
        except ValueError:
            print("Error: Por favor ingrese números válidos.")
    else:
        print("Opción no válida. Intente de nuevo.")
        
        