import pandas as pd
import xlrd
import openpyxl
from pandas import ExcelWriter
archivo=pd.read_excel('BI_Clientes06.xlsx',sheet_name='Hoja1')
data=pd.DataFrame(archivo,
                  columns=['CustomerKey','FirstName', 'TotalChildren'])
resultados1=data.dropna(axis=0)
destino=ExcelWriter('resultado1.xlsx')
resultados1.to_excel(destino,index=False)
destino.save()
print('Archivo creado correctamente');


##dropna elimina filas y columna, pero cuando solo se pasa axis=0 solo
# elimina en donde en alguna columna encuentre vacio o nulo