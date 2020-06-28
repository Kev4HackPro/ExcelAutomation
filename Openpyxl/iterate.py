import openpyxl as xl

wb = xl.load_workbook(filename='reviews-sample.xlsx', data_only=True)
sheet = wb.active

data = sheet['A1:C2']
print(data)