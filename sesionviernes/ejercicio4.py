def Es_triangulo(lado1, lado2, lado3):
 suma= (lado1 + lado2)
 if (suma > lado3):
    return "Es un triángulo"
 else:
    return  "No es un triángulo"
def main():
 print("ingrese los lados de un triángulo")   
 print("="*30)   
 lado1= float(input("Ingrese el lado 1 del triángulo: "))
 lado2= float(input("Ingrese el lado 2 del triángulo: "))
 lado3= float(input("Ingrese el lado 3 del triángulo: "))
 print(Es_triangulo(lado1, lado2, lado3))
 print(Es_triangulo)
 main()