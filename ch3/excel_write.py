import openpyxl

filename = 'stat_104102.xlsx'
book = openpyxl.load_workbook(filename)

sheet = book.active

for i in range(0, 9):
    total = int(sheet[str(chr(i+66))+'4'].value.replace(',', ''))
    seoul = int(sheet[str(chr(i+66))+'5'].value.replace(',', ''))
    output = total - seoul
    print('서울 제외 인구 = ', output)

    sheet[str(chr(i+66))+'22'] = output
    cell = sheet[str(chr(i+66))+'22']

    cell.font = openpyxl.styles.Font(size=14, color='FF0000')
    cell.number_format = cell.number_format

filename = 'population.xlsx'
book.save(filename)
print('ok')