nota1= int(input("Ingrese la primera nota: "))
nota2= int(input("Ingrese la segunda nota: "))
nota3= int(input("Ingrese la tercera nota: "))
suma= nota1 + nota2 + nota3
promedio= suma / 3

print(f"""calificacion 1: {nota1:>3}
calificacion 2: {nota2:>3}
calificacion 3: {nota3:>3}
{"promedio:":<15} {promedio:>3.0f}""")