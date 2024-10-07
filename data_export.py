import pandas as pd

# Ruta del archivo CSV ordenado
archivo_csv_ordenado = 'compras_autos_ordenados.csv'

try:
    # Leer el archivo CSV ordenado
    data_ordenada = pd.read_csv(archivo_csv_ordenado)

    # Crear un objeto ExcelWriter
    archivo_excel = 'compras_autos_total.xlsx'
    with pd.ExcelWriter(archivo_excel) as writer:
        # Exportar la hoja original
        data_ordenada.to_excel(writer, sheet_name='Datos Originales', index=False)
        print(f"Datos originales exportados a la hoja 'Datos Originales' en '{archivo_excel}'")

        # Obtener zonas únicas
        zonas = data_ordenada['Zona'].unique()

        # Exportar datos por cada zona a una hoja diferente
        for zona in zonas:
            data_zona = data_ordenada[data_ordenada['Zona'] == zona]
            data_zona.to_excel(writer, sheet_name=zona, index=False)
            print(f"Datos de la zona '{zona}' exportados a la hoja '{zona}' en '{archivo_excel}'")

except Exception as e:
    print(f"Error al exportar los datos: {e}")
