import pandas as pd

# Ruta del archivo TXT
archivo_txt = 'C:\\Users\\LUIS\\workspace\\autos_comprados\\compras_autos_peru.txt'
try:
    # Leer el archivo TXT
    data = pd.read_csv(archivo_txt, delimiter='|',encoding='cp1252')
    
    # Guardar los datos en un archivo CSV temporal
    archivo_csv = 'compras_autos_peru.csv'
    data.to_csv(archivo_csv, index=False)
    
    print(f"Datos leídos y guardados en {archivo_csv}")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
