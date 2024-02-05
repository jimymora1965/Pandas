import pandas as pd

datos = pd.Series([40, 55, 20], index=['Carlos', 'Lina', 'Jose'])

# Iterate through the Series and print index, name, and value
for indice, (nombre, valor) in enumerate(datos.items()):
    print(f"{indice}: Nombre: {nombre}, Edad: {valor}")

