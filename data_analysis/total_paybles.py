##### This script give sum of total paybles

import openpyxl

data_workbook = openpyxl.load_workbook('data.xlsx')
data_sheet = data_workbook["data"]

paybles = []

for column in data_sheet.iter_cols():
    column_name = column[0].value
    if column_name == 'Total Paybles':
        for i, cell in enumerate(column):
            if i > 0:
              paybles.append(cell.value)
print(f'Sum of total paybles is {sum(paybles)}')