#Control de acceso por edad
edad=int(input("Ingresa la edad del cliente. "))
if edad >=18:
    print("Pelicula para adultos")
elif edad >=13 and edad <18:
    print("Pelicula para adolescentes")
elif edad >=0 and edad <13:
    print("Pelicula para niños")        