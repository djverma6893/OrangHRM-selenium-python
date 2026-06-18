import openpyxl
file="C:\\Users\\HP\\Desktop\\OrangHRM-Selenium-python\\TestData\\LoginDDT.xlsx"
sheetname="Sheet1"
workbook = openpyxl.load_workbook(file)
sheet= workbook[sheetname]
sheet.cell(3,3).value = "pass"
workbook.save(file)