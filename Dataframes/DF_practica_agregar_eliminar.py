import pandas as pd

datos = {
"Curso": pd.Series(["Panaderia", "Fotografia", "Conduccion","Tecnologia"]),
"Alumno": pd.Series(["Erica","Valentina","Christian","Jimy"]),
"Semestre":pd.Series(["2°","1°","1°","7°"]),
"Ciudad": pd.Series(["Valledupar","Bogota","San Andres"])
}

data = pd.DataFrame(datos)
print(data)
print()
print("Agregando la columna 'Nota' con assign:\n")
#Agregando columna con assign
data = data.assign(Nota = pd.Series(["8","9","9","7"]))
print(data)
print()
# agregando columna "Altura"
print("Agrego columna 'Altura':")
print()
data["Altura"] = pd.Series([1.6,1.58,1.76,1.65])
print(data)
print()

#eliminando una columna
print()
print("Eliminando la fila Semestre:\n")

data = data.drop("Semestre", axis=1)
print(data)


