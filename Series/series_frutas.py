import pandas as pd

# Crear una Serie con datos y etiquetas de índice personalizadas
datos = {'Manzanas': 10, 'Plátanos': 5, 'Uvas': 8, 'Naranjas': 12}
serie_frutas = pd.Series(datos)

# Mostrar la Serie
print("Serie de Frutas:")
print(serie_frutas)
print()

# Acceder a elementos por etiqueta de índice
print("Número de Manzanas:", serie_frutas['Manzanas'])
print()

# Realizar operaciones aritméticas con la Serie
serie_doble = serie_frutas * 2
print("Doble de la Serie:")
print(serie_doble)
print()

# Filtrar elementos de la Serie
frutas_mas_de_8 = serie_frutas[serie_frutas > 8]
print("Frutas con más de 8 unidades:")
print(frutas_mas_de_8)
