import openpyxl

a = input('Enter your name: ')
b = input('Enter your surname: ')
c = input('Enter your age: ')

wb = openpyxl.Workbook()
sheet = wb.active


sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['C1'] = 'Age'
sheet['A2'] = a
sheet['B2'] = b
sheet['C2'] = c

wb.save('file_10.xlsx')
