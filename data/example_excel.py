#es necesario tener instalado pandas y  XlsxWriter
#conda install pandas
#pip install XlsxWriter

# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file_example = 'example.xlsx'

df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

writer = pd.ExcelWriter(file_example, engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

writer.save()
