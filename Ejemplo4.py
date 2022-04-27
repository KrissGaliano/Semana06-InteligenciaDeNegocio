import pandas as pd
import xlrd
import openpyxl
from pandas import ExcelWriter
import numpy as np
archivo=pd.read_excel('BI_Clientes06.xlsx',sheet_name='Hoja1')
data=pd.DataFrame(archivo)
print('Resumir los valores perdidos totales')
r1=data.isna().sum()
print(r1)
print('Valores duplicados')
r2=data.nunique()
print(r2)
print('Cantidad de veces que un cliente aparece en la data')
r3=data.groupby(by='CustomerKey').size().sort_values(ascending=False)
print(r3)
print('Eliminando valores duplicados')
r4=data.drop_duplicates()
print(r4)
destino=ExcelWriter('resultado4.xlsx')
r4.to_excel(destino,index=False)
destino.save()
print('Archivo creado')