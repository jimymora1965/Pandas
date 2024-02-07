import pandas as pd

datos = {
    "Nombre": pd.Series(["Jimy", "Erica", "Christian", "Valentina"]),
    "Edad": pd.Series([58, 45, 27, 24]),
    "Nacido": pd.Series(["Buenaventura", "Valledupar", "San Andres Isla", ""]),
    "Estudios": pd.Series(["Primaria", "Chef", "", ""])
}

# Agregar la serie "Ciudad" y "Religion" y "Peso en libras y peso en kilos" al diccionario de datos
datos["Ciudad"] = pd.Series(["San Andres", "Valledupar", "Bogota", "San Andres"])
datos["Religion"]= pd.Series(["Catolica","Catolica","Pentecostal","Hindu"])
datos["Peso"] = pd.Series([70,58,79,61])
datos["Peso en kilos"] = [peso * 2 for peso in datos["Peso"]]
data = pd.DataFrame(datos)
print(data)
print()
religion = data[data["Religion"]== "Hindu"]
print("\tReligiones\n")
print(religion)
 

