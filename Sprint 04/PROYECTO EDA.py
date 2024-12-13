#PROYECTO EDA

import yfinance as yf

# Listado de las empresas 
empresas = [
    'AAPL',   # Apple
    'MSFT',   # Microsoft
    'GOOGL',  # Alphabet
    'GE',     # General Electric
    'CAT',    # Caterpillar
    'PFE',    # Pfizer
    'JNJ',    # Johnson & Johnson
    'DE',     # Deere & Company
    'CCL'     # Carnival Corporation
]

# Descargar los datos de las empresas desde 2010 hasta el día de hoy con intervalo mensual
datos = {}

for empresa in empresas:
    # Descargar datos históricos
    data = yf.download(empresa, start='2010-01-01', interval='1mo')
    
    # Guardar los datos en el diccionario
    datos[empresa] = data

    # Exportar los datos de cada empresa a un archivo CSV
    data.to_csv(f'{empresa}_data.csv')

    print(f'Datos de {empresa} descargados correctamente.')

# Si deseas combinar todos los datos en un solo archivo CSV:
import pandas as pd

# Crear un DataFrame vacío
df_completo = pd.DataFrame()

# Concatenar todos los datos de las empresas en el DataFrame
for empresa, data in datos.items():
    # Asegurar que los datos tengan una columna 'Adj Close' para cada empresa
    df_completo[empresa] = data['Adj Close']

# Exportar el DataFrame completo a un solo CSV
df_completo.to_csv('empresas_datos_completos.csv')

print('Todos los datos han sido combinados y exportados a empresas_datos_completos.csv.')


