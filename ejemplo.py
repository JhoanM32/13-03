import pandas as pd
columnas = int(input("¿Cuántas columnas quieres?: "))
filas = int(input("¿Cuántas filas quieres?: "))
datos = {}
# Solicita el nombre de cada columna y sus valores
for c in range(columnas):
    nombre_col = input(f"Nombre de la columna {c+1}: ")
    datos[nombre_col] = []
    for f in range(filas):
         valor = input(f"Ingrese el valor de la fila {f+1}, columna'{nombre_col}': ")
         datos[nombre_col].append(valor)


df_usuario = pd.DataFrame(datos)
print("\nDataFrame creado:")
print(df_usuario)
print("\nDataFrame ordenado por la primera columna ingresada:")
print(df_usuario.sort_values(by=list(datos.keys())[0]))