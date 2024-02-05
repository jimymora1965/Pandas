import pandas as pd

datos = {
    "Nombre": pd.Series(["Jimy", "Erica", "Christian", "Valentina"]),
    "Edad": pd.Series(["58","45","27","24"]),
    "Nacido":pd.Series(["Buenaventura","Valledupar","San Andres Isla", ])
    }

data = pd.DataFrame(datos)
print(data)