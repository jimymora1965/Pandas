""" import pandas as pd

datos = {
    "Curso": pd.Series(["Cocina","Panaderia","Conduccion","Enfermeria"]),
    "Alumno": pd.Series(["Erica", "Valentina","Christian","jimy"]),
    "Aprobado":pd.Series(["Si","","No",""])
}

data = pd.DataFrame(datos)
print(data) """

#con este codigo lleno los espacios en blanco con NA(no aplica)

import pandas as pd

datos = {
    "Curso": pd.Series(["Cocina", "Panaderia", "Conduccion", "Enfermeria"]),
    "Alumno": pd.Series(["Erica", "Valentina", "Christian", "jimy"]),
    "Aprobado": pd.Series(["Si", "", "No", ""])
}

data = pd.DataFrame(datos)

# Reemplazar los valores vacíos en la columna "Aprobado" con la sigla "NA" (por ejemplo)
data["Aprobado"] = data["Aprobado"].replace("", "NA")

print(data)
