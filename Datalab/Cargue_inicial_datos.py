import pandas as pd

url = 'https://www.datos.gov.co/resource/gt2j-8ykr.json?$offset=' ##conexión con la fuente de datos

consolidated_files = pd.DataFrame() ##tabla donde se almacenarán los registros

length = 0
i = 0 ##acumulador para poder establecer el número del registro a leer (funciona junto con offset)

#En cada nueva iteración se leen 1000 registros (este es el máximo por iteración) comenzando por el último encontrado para no repetir
while length % 1000 == 0: ##mientras la cantidad de registros dividido mil no deje residuo significa que aún hay registros por extraer
    offset = str(i*1000) ##offset indica en qué registro comenzar
    df = pd.read_json(url+offset)
    consolidated_files = consolidated_files.append(df, sort=False) ##se agregan los nuevos datos a la tabla sin borrar los anteriores
    length = len(consolidated_files) ##se actualiza la cantidad de registros en la tabla para ser evaluada en la próxima iteración
    i = i + 1
    print('Cargados ' + str(length) + ' registros') ##validador en pantalla de ejecución
del df
print('Cargue completado: ' + str(length) + ' registros') ##validar finalización del cargue de los registros
consolidated_files.to_csv(r'../Datos/CasosPositivosCOVID19_Colombia.csv', index=False)