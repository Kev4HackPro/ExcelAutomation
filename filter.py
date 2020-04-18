import pandas as pd

df_csv = pd.read_csv('Names.csv', header=None)
df_csv.columns = ['First Name', 'Second Name', 'Street', 'City','State', 'Area code','Income']
df_csv['Tax%'] = df_csv['Income'].apply(lambda x: .15 if 10000 < x < 40000 else .20 if 40000 < x < 80000 else.25)
df_csv['Tax owed'] = df_csv['Income'] * df_csv['Tax%']
to_drop = ['Area code', 'First Name', 'Street']
df_csv.drop(columns=to_drop, inplace=True)
df_csv['Test col'] = False
df_csv.loc[df_csv['Income'] < 60000, 'Test col'] = True
print(df_csv)