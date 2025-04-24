litros_mes= int(input("Ingresar la cantidad total de litros consumidos en un mes en una vivienda"))
cant_personas= int(input("Ingresar la cantidad de personas que habitan en la vivienda"))
consumo_mensual= litros_mes / cant_personas
print(f"""Consumo mensual por persona: {consumo_mensual:>3}""")
consumo_diario= consumo_mensual / 30
print(f"""Consumo diario por persona: {consumo_diario:>3}""")