import os
import pandas as pd

# Directorio donde se encuentran los archivos CSV
path = '/home/serchiboi/Desktop/Docs/AllDocs'

# Lista para almacenar los DataFrames
dataframes = []

# Iterar sobre cada archivo en el directorio
for filename in os.listdir(path):
    if filename.endswith('.csv'):
        file_path = os.path.join(path, filename)
        # Leer el archivo CSV
        df = pd.read_csv(file_path, sep='|')
        # Añadir el DataFrame a la lista
        dataframes.append(df)

# Concatenar todos los DataFrames en uno solo
final_df = pd.concat(dataframes, ignore_index=True)

# Guardar el DataFrame resultante en un nuevo archivo CSV
final_df.to_csv(os.path.join(path, 'Final.csv'), index=False, sep='|')
