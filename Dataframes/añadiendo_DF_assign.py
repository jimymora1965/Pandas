import pandas as pd





datos = {
    "Curso": pd.Series(["Cocina", "Panaderia", "Conduccion", "Enfermeria"]),
    "Alumno": pd.Series(["Erica", "Valentina", "Christian", "jimy"]),
    "Aprobado": pd.Series(["Si", "", "No", ""])
}

data = pd.DataFrame(datos)

# Reemplazar los valores vacíos en la columna "Aprobado" con la sigla "NA" (por ejemplo)
data["Aprobado"] = data["Aprobado"].replace("", "NA")

# Usar el método assign para agregar una nueva columna llamada "Nota" con valores predeterminados
data = data.assign(Nota=pd.Series([8, 7, 5, 6]))

print(data)
