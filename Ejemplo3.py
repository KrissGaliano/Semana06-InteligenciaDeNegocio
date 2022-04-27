import pandas as pd
import xlrd
import openpyxl
from pandas import ExcelWriter
import numpy as np
archivo=pd.read_excel('BI_Clientes06.xlsx',sheet_name='Hoja1')
data=pd.DataFrame(archivo,columns=['TotalChildren'])
prom=data['TotalChildren'].mean()
resultados3=data['TotalChildren'].replace(np.nan,prom)
destino=ExcelWriter('resultado3.xlsx')
resultados3.to_excel(destino,index=False)
destino.save()
print('Archivo creado correctamente(3)');





#replace() --> se encarga de modificar los datos actuales por un nuevo valor.