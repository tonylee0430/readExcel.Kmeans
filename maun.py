import pandas as pd
import numpy

file_path = '/Users/tony/desktop/2330.xlsx'
sheet = pd.read_excel(file_path, sheetname='sheet1')

def getRows():
    rows = []
    for row in sheet.values:
        rows.append(row)
    return rows



rows = getRows()

def filter( rows ):

    j = 0
    a = []

    for i in rows:
        x=numpy.delete(i,0,0)
        x=numpy.delete(x,6,0)
        a.append(x)

    return a




result = filter(rows)
print result


