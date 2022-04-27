import pandas as pd
import xlrd
import openpyxl
from pandas import ExcelWriter
archivo=pd.read_excel('BI_Clientes06.xlsx',sheet_name='Hoja1')
data=pd.DataFrame(archivo,
                  columns=['CustomerKey','FirstName', 'TotalChildren'])
resultados2=data.dropna(subset=['TotalChildren'],axis=0)
destino=ExcelWriter('resultado2.xlsx')
resultados2.to_excel(destino,index=False)
destino.save()
print('Archivo creado correctamente(2)');


##dropna eliminar filas y columna, pero cuando solo se pasa axis=0 solo
# elimina en donde en alguna columna encuentre vacio o nulo

#Pero si queremos que busque el dato nulo, puntualmente en una sola fila para eso
#utilizamos subset

#ExcelWrite; para crear un archivo de lectura y escritura

#para escribir los datos de la variable sobre una variable de destino que representa un nuevo archivo excel


