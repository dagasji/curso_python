import pandas as pd

fichero_csv = "catalogo_cf.csv"
# leer_csv = pd.read_csv(fichero_csv, encoding="ISO-8859-1")

# leer_csv.to_excel(r"catalogo_cf.xlsx", index=None, header=True)

# Se crea el dataframe con pandas de un fichero Excel
dataframe_excel = pd.read_excel("catalogo_cf.xlsx")
print(dataframe_excel)

# Selecciona la primera y la cuarta columna
print(dataframe_excel.iloc[[1-4], [1, 3]])

# se exporta a excel
dataframe_excel.iloc[[1-4], [1, 3]].to_excel('catalogo_cf_resumen.xlsx')