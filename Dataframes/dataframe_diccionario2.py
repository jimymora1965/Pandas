import pandas as pd

datos = {
    "Curso": pd.Series(["Cocina","Panaderia","Conduccion","Enfermeria"]),
    "Alumno": pd.Series(["Erica", "Valentina","Christian","jimy"]),
    "Aprobado":pd.Series(["Si","","No",""])
}

data = pd.DataFrame(datos)
print(data)