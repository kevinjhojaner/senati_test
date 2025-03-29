import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#carga el archivo cvs
df = pd.read_csv("ventas_ficticias.csv")

#exploracion de la estructura del archivo
print("Información del DataFrame:")
df.info()
print(f"\nNúmero de filas y columnas: {df.shape}")
print(f"\nTipos de datos:\n{df.dtypes}")
print(f"\nPrimeras filas:\n{df.head()}")
print(f"\nÚltimas filas:\n{df.tail()}")


#manejo de valores nulos y datos faltantes
print ("\nValores nulos por columna: ")
print (df.isnull().sum())

print("\nDatos después de manejar valores nulos:")
print(df.info())

#aplicar operaciones con numpy para metricas
suma_total_venta = np.sum(df["Total Venta"])
promedio_total_venta = np.mean(df["Total Venta"])
mediana_total_venta = np.median(df["Total Venta"])
desviacion_total_venta = np.std(df["Total Venta"])

print(f"\nMétricas calculadas con NumPy:\n"
      f"Promedio de Total Venta: {promedio_total_venta:.2f}\n"
      f"Mediana de Total Venta: {mediana_total_venta:.2f}\n"
      f"Desviación estándar de Total Venta: {desviacion_total_venta:.2f}\n"
      f"Suma total de ventas: {suma_total_venta:.2f}")

#REALZIAR ANALISIS DESCRIPTIVO UTILIZANDO ESTADISTICAS BASICAS
print("Estadisticas descriptivas: ")
print(df.describe())

#IDENTIFICAR PATRONES Y CORRELACIONES DENTRO DE LOS DATOS
df_corr = df.select_dtypes(include=[np.number]).corr()
print ("\nCorrelaciones entre variables: ")
print (df_corr)

# Visualización del mapa de calor de correlaciones

plt.figure(figsize=(10, 6))
sns.heatmap(df_corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Mapa de Calor de Correlaciones")
plt.show()

#APLICAR FILTROS Y SEGMENTACION RELEVANTES
#filtrar ventas mayores a un umbral
umbral_venta = 1000
df_filtrado = df[df["Total Venta"] > umbral_venta]
print (f"\nVenta mayores a {umbral_venta}:\n", df_filtrado)

#filtrar por categoria especifica
categoria_filtro = "Electronica"
df_categoria = df[df["Categoria"] == categoria_filtro]
print(f"\nProductos en la categoría '{categoria_filtro}':\n", df_categoria)

#filtrar ventas por cliente especifico
cliente_filtro = "Toni Sanchez"
df_cliente = df[df["Cliente"] == cliente_filtro]
print(f"\nVentas del cliente '{cliente_filtro}':\n", df_cliente)


df["Fecha de Venta"] = pd.to_datetime(df["Fecha de Venta"])


# Ordenar los datos por fecha para evitar desorden en el gráfico
df = df.sort_values("Fecha de Venta")

#VIZUALIACION DE DATOS

#graficos de lineas: Evolucion de ventas en el tiempo
plt.figure(figsize=(10, 5))
plt.plot(df["Fecha de Venta"], df["Total Venta"], marker="o", linestyle="-")
plt.xlabel("Fecha de Venta")
plt.ylabel("Total Venta")
plt.title("Evolucion de ventas en el tiempo")
plt.xticks(rotation=45)
plt.grid()
plt.show()

#grafico de barras: Ventas por categoria
plt.figure(figsize=(8, 5))
df.groupby("Categoria")["Total Venta"].sum().plot(kind="bar", color="skyblue")
plt.xlabel("Categoría")
plt.ylabel("Total Venta")
plt.title("Ventas Totales por Categoría")
plt.xticks(rotation=45)
plt.show()

#grafico de torta: proporcion de ventas por categoria
df_categoria_sum = df.groupby("Categoria")["Total Venta"].sum()
plt.figure(figsize=(6, 6))
plt.pie(df_categoria_sum, labels=df_categoria_sum.index, autopct="%1.1f%%", colors=["blue", "green", "red", "purple"])
plt.title("Distribución de Ventas por Categoría")
plt.show()

#histograma: Distribucion de montos de venta
plt.figure(figsize=(8, 5))
plt.hist(df["Total Venta"], bins=10, color="orange", edgecolor="black")
plt.xlabel("Total Venta")
plt.ylabel("Frecuencia")
plt.title("Distribución de Montos de Venta")
plt.show()