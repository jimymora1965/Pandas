""" import pandas as pd

datos = {
    "Nombre": pd.Series(["Jimy", "Erica", "Christian", "Valentina"]),
    "Edad": pd.Series([58, 45, 27, 24]),
    "Nacido": pd.Series(["Buenaventura", "Valledupar", "San Andres Isla", ""]),
    "Estudios": pd.Series(["Primaria", "Chef", "", ""])
}

data = pd.DataFrame(datos)
print(data)
 """

print("Para imprimir solo la columna Nombre: ")
import pandas as pd
datos = {
    "Nombre": pd.Series(["Jimy", "Erica", "Christian", "Valentina"]),
    "Edad": pd.Series([58, 45, 27, 24]),
    "Nacido": pd.Series(["Buenaventura", "Valledupar", "San Andres Isla", ""]),
    "Estudios": pd.Series(["Primaria", "Chef", "", ""])
}

data = pd.DataFrame(datos)

# Imprimir solo la columna "Nombre"
nombres = data["Nombre"]
print("Nombres:")
print(nombres)
