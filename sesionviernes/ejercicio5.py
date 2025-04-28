edad= int(input("Ingrese la edad de la persona"))
if edad >= 18 and edad < 60:
    print("La persona es mayor de edad")
elif edad >= 0 and edad < 12:
    print("La persona es un niño")    
elif edad >=12 and edad < 18:
    print("La persona es un adolescente") 
elif edad >=60 and edad < 100:
    print("La persona es un adulto mayor")