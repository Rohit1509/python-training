##### This script gives a total number of transformers sold and total paybles from transformers

import openpyxl
import matplotlib.pyplot as plt

data_workbook = openpyxl.load_workbook('data.xlsx')
data_sheet = data_workbook["data"]

total_transformers_sold = {}

for column in data_sheet.iter_cols():
    column_name = column[0].value
    if column_name == 'Type of product':
        for i, cell in enumerate(column):
            if i > 0 and cell.value == 'Transformer':
              total_transformers_sold.update({data_sheet.cell(row=i+1, column=6).value:data_sheet.cell(row=i+1, column=16).value})

total_number_transformers_sold = len(list(total_transformers_sold.keys()))
total_paybles_from_transformers = sum(list(total_transformers_sold.values()))

print(f'Total number of transformers sold are {total_number_transformers_sold}')
print(f'Total paybles received from transformers are {total_paybles_from_transformers}')

