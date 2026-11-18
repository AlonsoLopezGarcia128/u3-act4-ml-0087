# Alonso Lopez Garcia NC = 0087 | Fecha 18/11/2026
import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear diccionario con datos de registro de plagas
registro_plagas = {
    'id_registro': [401, 402, 403, 404, 405, 406],
    'parcela': ['El Mirador', 'La Esperanza', 'San Jose', 'El Roble', 'La Pradera', 'Los Pinos'],
    'fecha_deteccion': ['2023-06-15', '2023-11-01', '2023-07-10', '2023-08-05', '2023-09-20', '2023-11-15'],
    'tipo_plaga': ['Gusano cogollero', 'Afid', 'Mosca blanca', 'Chicharrita', 'Pulgón', 'Afid'],
    'nivel_infestacion': ['Alto', 'Medio', 'Bajo', 'Medio', 'Alto', 'Bajo'],
    'area_afectada_porcentaje': [30, 15, 5, 20, 40, 10],
    'accion_tomada': ['Fumigacion', 'Control biologico', 'Monitoreo', 'Fumigacion', 'Fumigacion', 'Control biologico'],
    'producto_aplicado': ['Clorpirifos', 'Jabon potasico', 'Ninguno', 'Imidacloprid', 'Lambda-cialotrina', 'Jabon potasico'],
    'costo_control': [2500, 800, 0, 1500, 3500, 600],
    'resultado': ['Controlado', 'Controlado', 'Controlado', 'En observacion', 'Controlado', 'Controlado']
}

print(" --- Análisis Exploratorio de Datos ---") 
print("EDA, Exploratory Data Analysis --- por Alonso Lopez Garcia NC = 0087")
print("Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(registro_plagas)
print(" --- TABLA ORIGINAL DE REGISTRO DE PLAGAS ---")
print(df)

# 3. Exportar los datos a CSV
print(" --- Convertir el DataFrame en archivo CSV ---")
df.to_csv(
    "registro_plagas_0087.csv",
    index=False,
    encoding="utf-8-sig"
)
print("✅ Archivo CSV creado correctamente")
print(" ")
print(" --- 8. Leer los datos desde el archivo CSV --- ")
print("registro_plagas_0087.csv")

# 4. Leer el archivo CSV
df = pd.read_csv("registro_plagas_0087.csv")
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
print(" ")
print(" --- 9. Análisis Exploratorio de Datos (EDA) ---")

# 5. Primeros y últimos registros
print(" --- 1. PRIMEROS REGISTROS (Head): ---")
print(df.head(3)) # Muestra los primeros 3
print(" --- 2. ÚLTIMOS REGISTROS (Tail): ---")
print(df.tail(2)) # Muestra los últimos 2

# 6. Dimensiones y estructura
print(" --- 6. Dimensiones y estructura ---")
print(df) # Mostrar tabla o matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)

print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("\n7. ESTADÍSTICAS DESCRIPTIVAS:")
print(df.describe())

print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())

print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())

print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Tipos de plaga únicos:", df["tipo_plaga"].unique())

# 8. Análisis específico
print(df)
print("-----------------------------------------------------")
print("\n11. REGISTROS POR TIPO DE PLAGA:")
print(df["tipo_plaga"].value_counts())

print("\n12. PROMEDIO DE COSTO DE CONTROL: $", df["costo_control"].mean())
print("13. COSTO DE CONTROL MÁXIMO: $", df["costo_control"].max())
print("14. COSTO DE CONTROL MÍNIMO: $", df["costo_control"].min())

# 9. Ordenamiento, filtrado y agrupación
print(" --- 9. Ordenamiento, filtrado y agrupación --- ")
print(" --- 15. REGISTROS ORDENADOS POR COSTO DE CONTROL (Mayor a menor): ---")
print(df.sort_values(by="costo_control", ascending=False))

print("\n16. REGISTROS CON COSTO DE CONTROL MAYOR A $1,000:")
filtro = df[df["costo_control"] > 1000]
print(filtro)

print("\n17. RESUMEN POR ACCIÓN TOMADA:")
resumen = df.groupby("accion_tomada").agg(
    registros=("id_registro", "count"),
    costo_promedio=("costo_control", "mean"),
    area_maxima_afectada=("area_afectada_porcentaje", "max")
)
print(resumen)

# 18. Gráfica de barras: Registros por acción tomada
print("18. Gráfica de barras: Registros por acción tomada")
conteo = df["accion_tomada"].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color="skyblue")
plt.title("Registros por acción tomada | Alonso Lopez NC = 0087")
plt.xlabel("Acción tomada")
plt.ylabel("Cantidad de registros")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Costo de control por parcela
print("19. Gráfica de barras: Costo de control por parcela")
plt.figure(figsize=(8, 5))
plt.bar(df["parcela"], df["costo_control"], color="lightgreen")
plt.title("Costo de control por parcela | EDA Alonso Lopez NC = 0087")
plt.xlabel("Parcela")
plt.ylabel("Costo en pesos")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución del área afectada (%)
print("20. Histograma: Distribución del área afectada")
plt.figure(figsize=(8, 5))
plt.hist(df["area_afectada_porcentaje"], bins=5, color="orange", edgecolor="black")
plt.title("Distribución de área afectada (%) | EDA Alonso Lopez NC = 0087")
plt.xlabel("Área afectada (%)")
plt.ylabel("Frecuencia")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Área afectada vs Costo de control
print("21. Gráfica de dispersión: Área afectada vs Costo de control")
plt.figure(figsize=(8, 5))
plt.scatter(df["area_afectada_porcentaje"], df["costo_control"], color="red", s=100)
plt.title("Relación entre área afectada y costo de control | EDA Alonso Lopez NC = 0087")
plt.xlabel("Área afectada (%)")
plt.ylabel("Costo de control ($)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de costos de control
print("22. Diagrama de caja: Distribución de costos de control")
plt.figure(figsize=(7, 5))
plt.boxplot(df["costo_control"], patch_artist=True, boxprops=dict(facecolor="lightblue"))
plt.title("Distribución de costos de control (Boxplot) | EDA Alonso Lopez NC = 0087")
plt.ylabel("Costo de control ($)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
print("23. Matriz de correlación")
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title("Matriz de correlación de variables numéricas | EDA Alonso Lopez NC = 0087")
plt.tight_layout()
plt.show()

print(" ")
print("Alonso Lopez Garcia NC = 0087 | Fecha 18/11/2026")