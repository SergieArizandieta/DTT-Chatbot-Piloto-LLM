import os
import pandas as pd
path = '/home/serchiboi/Desktop/Docs/TodosDocumentos/Final.csv'



# Leer el archivo CSV
df = pd.read_csv(path, sep='|')
print(df.head())

# Trying another approach by filtering for questions with keywords related to "práctica inicial" or "tiempo"
respuesta_practica_inicial_tiempo = df[df['Pregunta'].str.contains("práctica inicial|tiempo|duración", case=False)]

# Display the filtered result
print("============")
print(respuesta_practica_inicial_tiempo.head())
