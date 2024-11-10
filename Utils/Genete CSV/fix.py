import csv
path = '/home/serchiboi/Desktop/Docs/TodosDocumentos/'

# Lee el archivo original y escribe un nuevo archivo con comillas en cada campo
with open(path+'Final.csv', 'r', encoding='utf-8') as infile, open(path+'archivo_con_comillas.csv', 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile, delimiter='|')
    writer = csv.writer(outfile, delimiter='|', quoting=csv.QUOTE_ALL)

    # Copia cada fila del archivo original al nuevo archivo con comillas
    for row in reader:
        writer.writerow(row)

print("Archivo creado con comillas en cada campo: archivo_con_comillas.csv")
