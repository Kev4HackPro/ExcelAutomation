import pandas as pd
from openpyxl.workbook import Workbook
df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv', header=None)
df_txt = pd.read_csv('data.txt',delimiter='\t')

print(df_txt)

df_csv.columns = ['First Name', 'Second Name', 'Street', 'City','State', 'Area code','Income']
df_csv.to_excel('modified.xlsx', index=None)