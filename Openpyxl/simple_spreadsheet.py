from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet['A1'] = 'Hello'
sheet['B1'] = 'Excel'

workbook.save(filename='spread_create.xlsx')