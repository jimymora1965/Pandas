import pandas as pd

datos = {
    "Nombre": pd.Series(["Jimy", "Erica", "Christian", "Valentina"]),
    "Edad": pd.Series([58, 45, 27, 24]),
    "Nacido": pd.Series(["Buenaventura", "Valledupar", "San Andres Isla", ""]),
    "Estudios": pd.Series(["Primaria", "Chef", "", ""]),
    "Ciudad": pd.Series(["San Andres", "Valledupar", "Bogota", "San Andres"]),
    "Religion": pd.Series(["Catolica", "Catolica", "Pentecostal", "Hindu"]),
    "Peso": pd.Series([70, 58, 79, 61]),
    "Peso en kilos": pd.Series([140, 116, 158, 122])
}

data = pd.DataFrame(datos)

# Imprimir solo los datos de "Erica"
erica_data = data[data["Nombre"] == "Erica"]
print("\tDatos de Erica\n")
print(erica_data)
