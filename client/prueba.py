import random

# Cargar los IDs desde el archivo de entrada
with open('skus.txt', 'r') as archivo:
    ids = [line.strip() for line in archivo.readlines()]

# Definir la media y la desviación estándar para la distribución normal
media = len(ids) // 2
desviacion_estandar = len(ids) // 3

# Generar 10 consultas basadas en la distribución normal
consultas_generadas = []
for _ in range(1000):
    # Usar la distribución normal para elegir un índice
    indice = int(random.normalvariate(media, desviacion_estandar))
    # Asegurarse de que el índice esté dentro de los límites
    indice = max(0, min(indice, len(ids) - 1))
    consulta = ids[indice]
    consultas_generadas.append(consulta)

# Guardar las consultas en un archivo de salida
with open('sku_distribution.txt', 'w') as archivo:
    for consulta in consultas_generadas:
        archivo.write(consulta + '\n')
