inv_inicial=int(input("Ingrese la cantidad inicial del inventario"))
productos_recibidos=int(input("Ingrese la cantidad de productos recibidos"))
productos_vendidos=int(input("Ingrese la cantidad de productos vendidos"))
suma= inv_inicial+productos_recibidos
restante= suma-productos_vendidos
inv_actual: print(f"""inventario actual: {restante:>3}
inventario inicial: {inv_inicial:>3}
productos vendidos: {productos_vendidos:>3}                       
productos recibidos: {productos_recibidos:>3}
inv_final: {restante:>3}""")