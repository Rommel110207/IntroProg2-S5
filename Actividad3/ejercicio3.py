cap_inicial=float(input("Ingrese el capital: "))
interes_anual=float(input("Ingrese el interes anual en %: "))
años=int(input("Ingrese el numero de años: "))
tasa_decimal= interes_anual / 100
monto_final= ((1+tasa_decimal) ** años) * cap_inicial
interes_ganado= monto_final - cap_inicial
print(f"""Capital inicial: {cap_inicial:>3}´""")
print(f"Interes anual: {interes_anual:>3}%")
print(f"Años: {años:>3}")
print(f"Interes ganado: {interes_ganado:>3}")