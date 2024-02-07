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

# Eliminar la columna "Alumno"
data = data.drop("Alumno", axis=1)

print(data)
