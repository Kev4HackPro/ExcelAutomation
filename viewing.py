import pandas as pd
from openpyxl.workbook import Workbook

df_csv = pd.read_csv('Names.csv')
df_csv.columns = ['First Name', 'Second Name', 'Street', 'Address','City', 'State','Area code']
# print(df_csv[['State','Area code']])
# print(df_csv['City'][0:3])
print(df_csv.iloc[1,1])
wanted_values = df_csv[['Address', 'City', 'State']]
stored = wanted_values.to_excel('Location.xlsx', index=None)