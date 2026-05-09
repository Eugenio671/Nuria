import pandas as pd
import matplotlib.pyplot as plt

archivo = "ventas.csv"
# archivo = "tarea compu.xlsx"

# detectar tipo de archivo
if archivo.endswith(".csv"):
    df = pd.read_csv(archivo, encoding="latin-1")
elif archivo.endswith(".xlsx"):
    df = pd.read_excel(archivo)
else:
    raise ValueError("Formato de archivo no compatible")

# limpiar nombres de columnas
df.columns = df.columns.str.strip()

# ver primeras filas e información
print(df.head())
print(df.info())
print(df.columns)

# procesamiento
df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
df["Peso (kg)"] = pd.to_numeric(df["Peso (kg)"], errors="coerce")
df["precio"] = pd.to_numeric(df["precio"], errors="coerce")

# nueva columna
df["ingreso"] = df["Peso (kg)"] * df["precio"]

print(df)

# análisis de datos
total_ingreso = df["ingreso"].sum()
print("Ingreso total:", total_ingreso)

# producto más vendido
ventasproducto = df.groupby("Producto")["Peso (kg)"].sum()
print(ventasproducto)

# ventas por día
ventas_dia = df.groupby("Fecha")["ingreso"].sum()
print(ventas_dia)

# visualización
ventasproducto.plot(kind="bar", title="Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Peso vendido (kg)")
plt.tight_layout()
plt.show()