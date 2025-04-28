# Solicitar una letra de calificación al usuario
calificacion = input("Introduce una letra de calificación (A, B, C, D, F): ").upper()

# Mostrar el significado según el sistema estadounidense
if calificacion == "A":
    print("Excelente")
elif calificacion == "B":
    print("Bueno")
elif calificacion == "C":
    print("Promedio")
elif calificacion == "D":
    print("Debajo del promedio")
elif calificacion == "F":
    print("Reprobado")
else:
    print("Calificación no válida")
