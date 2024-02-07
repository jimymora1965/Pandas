import pandas as pd

datos = {
    "Curso": pd.Series(["Cocina", "Panaderia", "Conduccion", "Enfermeria"]),
    "Alumno": pd.Series(["Erica", "Valentina", "Christian", "jimy"]),
    "Aprobado": pd.Series(["Si", "", "No", ""])
}

data = pd.DataFrame(datos)
data = data.assign(Nota=pd.Series([8, 7, 5, 6]))

# Reemplazar los valores vacíos en la columna "Aprobado" con la sigla "NA" (por ejemplo)
data["Aprobado"] = data["Aprobado"].replace("", "NA")

# Imprimir el DataFrame antes de eliminar la fila
print("DataFrame antes de eliminar la fila:")
print(data)

# Eliminar la primera fila del DataFrame (índice 0)
data = data.drop(data.index[0])

# Imprimir el DataFrame después de eliminar la fila
print("\nDataFrame después de eliminar la fila:")
print(data)
