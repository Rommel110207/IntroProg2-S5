Distancia= float(input("Introduce la distancia en km: "))
litros_consumidos= float(input("Introduce los litros consumidos: "))
redimiento= (Distancia/litros_consumidos)
print(f"El rendimiento es de {redimiento:.2f} km/litro")
gasto_total_combustible= (litros_consumidos*Distancia)/100
print(f"El gasto total de combustible es de {gasto_total_combustible:.2f} litros")
print(f"el rodamiento es de {redimiento:.2f} km/litro")
print(f"El gasto total de combustible es de {gasto_total_combustible:.2f} litros")