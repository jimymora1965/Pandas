import pandas as pd

altura = {"Santiago":187,"Maria": 150,"Carlos": 174,"Christian": 172}
datos = pd.Series(altura)
print()
datos2 = pd.Series(altura,index = ["Maria", "Carlos"])
print(datos)

print("\n\tMostrar indices que yo desee en la serie:")
print(datos2)