import openpyxl

filename = 'stat_104102.xlsx'
book = openpyxl.load_workbook(filename)

sheet = book.worksheets[0]

data = []
for row in sheet.rows:
    if row[9].value == None:
        continue
    data.append([
        row[0].value,
        int(row[9].value.replace(',', ''))
    ])

del data[0:2]

data = sorted(data, key=lambda x : x[1])

for i, a in enumerate(data):
    if (i >=5 ):
        break
    print(i+1, a[0], a[1])