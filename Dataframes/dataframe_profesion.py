import pandas as pd

datos = {
    "Nombre": pd.Series(["Erica", "Jimy"]),
    "Profesion": pd.Series(["Chef", "Medico"])
}

data = pd.DataFrame(datos)

# Filtrar el DataFrame para devolver solo las filas donde la profesión sea "Medico"
profesion = data[data["Profesion"] == "Medico"]

print("Solo imprimir la profesion:")
print(profesion)
