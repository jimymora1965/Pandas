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

""" print("Para imprimir solo la columna Nombre: ")
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
 """

""" print("Imprimir edades mayores a 30 años")
import pandas as pd

datos = {
    "Nombre": pd.Series(["Jimy", "Erica", "Christian", "Valentina"]),
    "Edad": pd.Series([58, 45, 27, 24]),
    "Nacido": pd.Series(["Buenaventura", "Valledupar", "San Andres Isla", ""]),
    "Estudios": pd.Series(["Primaria", "Chef", "", ""])
}

data = pd.DataFrame(datos)

# Filtrar el DataFrame para devolver solo las edades mayores a 30

mayores_a_30 = data[data["Edad"] > 30]

print("Edades mayores a 30:")
print(mayores_a_30) """



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
