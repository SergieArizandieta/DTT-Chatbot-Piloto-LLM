import os
import pandas as pd

# Directorio donde se encuentran los archivos CSV
path = '/home/serchiboi/Desktop/Docs/AllDocs/Final.csv'

df = pd.read_csv(path, sep='|')

max_len = 0
# Iterar a través de cada fila
for index, row in df.iterrows():
    # Acceder a los valores de cada columna en la fila actual
    columna1 = row['Question']
    columna2 = row['Answer']
    # Hacer algo con los valores de las columnas
    text = f"Question: {columna1}\Answer: {columna2}"
    max_len = max(max_len, len(text))

print(f"La longitud máxima de la cadena es: {max_len}")