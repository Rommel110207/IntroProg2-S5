# Solicitar al usuario que ingrese una temperatura en grados Celsius
temperatura = float(input("Ingresa la temperatura en grados Celsius: "))

# Clasificar el clima según la temperatura
if temperatura < 10:
    print("El clima es frío.")
elif 10 <= temperatura < 20:
    print("El clima es templado.")
elif 20 <= temperatura < 30:
    print("El clima es cálido.")
else:
    print("El clima es muy caluroso.")