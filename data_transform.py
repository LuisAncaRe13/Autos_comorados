import pandas as pd

# Ruta del archivo CSV intermedio
archivo_csv = 'compras_autos_peru.csv'

try:
    # Leer el archivo CSV
    data = pd.read_csv(archivo_csv)
    
    
    #Ordenar por departamentos
    data_ordenada = data.sort_values (by=['Año','Marca','Modelo','Zona','Ciudad','Método de Pago'])
       
    # Exportar a csv
    archivo_csv = 'compras_autos_ordenados.csv'
    data_ordenada.to_csv(archivo_csv, index=False)
    
    
    print(f"Datos exportados exitosamente a {archivo_csv}")

# Ruta del archivo CSV ordenado
    archivo_csv = 'compras_autos_peru.csv'

    # Leer el archivo CSV ordenado
    data_ordenada = pd.read_csv(archivo_csv)
    
    # Obtener zonas únicas
    zonas = data_ordenada['Zona'].unique()

    # Exportar datos por cada zona
    for zona in zonas:
        data_zona = data_ordenada[data_ordenada['Zona'] == zona]
        archivo_csv_zona = f'compras_autos_{zona}.csv'
        data_zona.to_csv(archivo_csv_zona, index=False)
        print(f"Datos de la zona '{zona}' exportados a '{archivo_csv_zona}'")       
        
except Exception as e:
    print(f"Error al transformar los datos: {e}")