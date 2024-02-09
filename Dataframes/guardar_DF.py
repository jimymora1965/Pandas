import pandas as pd

datos = {
    "Nombre": pd.Series(["Jimy", "Erica", "Christian", "Valentina"]),
    "Edad": pd.Series([58, 45, 27, 24]),
    "Nacido": pd.Series(["Buenaventura", "Valledupar", "San Andres Isla", "Bogotá"]),
    "Estudios": pd.Series(["Primaria", "Chef", "", ""]),
    "Ciudad": pd.Series(["San Andres", "Valledupar", "Bogota", "San Andres"]),
    "Religion": pd.Series(["Catolica", "Catolica", "Pentecostal", "Hindu"]),
    "Peso": pd.Series([70, 58, 79, 61])
}

# Agregar nuevas columnas al diccionario de datos
datos["Universidad"] = pd.Series(["Javeriana", "Mariano Moreno", "EIA", "EAS"])
datos["Hobbies"] = pd.Series(["Cine", "Tejidos", "Videojuegos", "Fotografia"])
datos["Salario"] = pd.Series([2000, 2500, 1800, 2200])
datos["Subsidio_Transporte"] = pd.Series([100, 150, 100, 150])
datos["Total_devengado"] = datos["Salario"] + datos["Subsidio_Transporte"]
datos["Peso_en_kilos"] = [peso * 2 for peso in datos["Peso"]]

data = pd.DataFrame(datos)

# Guardar como JSON
data.to_json("datos.json", orient="records")

# Guardar como CSV
data.to_csv("datos.csv", index=False)

# Guardar como HTML
data.to_html("datos.html", index=False)

print(data)
