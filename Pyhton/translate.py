import pandas as pd
from deep_translator import GoogleTranslator


MainFolder = '/home/serchiboi/Desktop/Docs/Utiles/SLA'
CSV = MainFolder + '/preguntas.CSV'
EngCSV = MainFolder + '/question.csv' 

df = pd.read_csv(CSV, sep='|')
print("Contenido original del CSV:")
print(df)


def translate_text(text):
        try:
            print("Traduciendo:",text,"--",type(text))
            # Intenta traducir el texto
            src = 'es' 
            dest = 'en' 
            #print(src,"--",dest)
            translated_text = GoogleTranslator(source=src, target=dest).translate(text) 
            print("Resultado:",translated_text,type(translated_text))
            return translated_text
        except Exception as e:
            #print(f"Error al traducir:{text} --->{e}")
            return "Tuve un problema de traducción ¿puedes volver a preguntar?"  # En caso de error, devuelve el texto original
        

# Aplica la función de traducción a todas las columnas del DataFrame
df_translated = df.apply(lambda x: x.apply(translate_text))

# print("\nContenido traducido del CSV:")
print(df_translated)

# Puedes guardar el DataFrame traducido en otro archivo CSV si lo deseas
df_translated.to_csv(EngCSV, index=False, sep='|')