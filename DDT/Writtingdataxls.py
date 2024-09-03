import openpyxl

file = "C:\Readingdata.selenium.xlsx"

workbook = openpyxl.load_workbook(file)
Sheet1 = workbook.active # get active sheet from excel
#Sheet1=workbook["Data"] #we can write this line also instead of above line


for r in range(1,6):
    for c in range(1,4):
        Sheet1.cell(r,c).value="Abhaya"
workbook.save(file)