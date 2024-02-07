import pandas as pd

datos = {
    "Alumno": pd.Series(["Erica", "Valentina", "Christian", "jimy"]),
    "Curso": pd.Series(["Cocina", "Panaderia", "Conduccion", "Enfermeria"]),   
    "Aprobado": pd.Series(["No", "Si"])
}

data = pd.DataFrame(datos)

print(data)

# Acceder a los datos de "Erica" utilizando loc[]
datos_erica = data[data['Alumno'] == "Erica"]
print("\nDatos de 'Erica':")
print(datos_erica)
