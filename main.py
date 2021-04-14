import datetime  
import  openpyxl as opxl

# print(datetime.date.today())
# f=open('Book.xlsx','r')
# print(f.read())
# f.close()


wb=opxl.load_workbook('Book.xlsx')
ws=wb['Sheet1']
# c=ws['A1':'A4']
# print(wb['A1'.value])
# read
for row in ws.iter_rows():
    for cell in row:
        print(cell.value)