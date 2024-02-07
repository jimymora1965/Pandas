import pandas as pd

datos = {
    "Curso": pd.Series(["Panaderia", "Fotografia", "Conduccion", "Tecnologia"]),
    "Alumno": pd.Series(["Erica", "Valentina", "Christian", "Jimy"]),
    "Semestre": pd.Series(["2°", "1°", "1°", "7°"]),
    "Ciudad": pd.Series(["Valledupar", "Bogota", "San Andres"])
}

data = pd.DataFrame(datos)

print(data)
print()

print("Agregando la columna 'Nota' con assign:\n")
data = data.assign(Nota=pd.Series(["8", "9", "9", "7"]))
print(data)
print()

print("Agrego columna 'Altura':\n")
data["Altura"] = pd.Series([1.6, 1.58, 1.76, 1.65])
print(data)
print()

# Dividir la altura entre 2 y mostrar el resultado en una nueva columna llamada "Altura_dividida"
data["Altura_dividida"] = data["Altura"] / 2
print("DataFrame con la columna 'Altura_dividida':\n")
print(data)
print()

# Eliminando la columna "Semestre"
print("Eliminando la columna 'Semestre':\n")
data = data.drop("Semestre", axis=1)
print(data)
