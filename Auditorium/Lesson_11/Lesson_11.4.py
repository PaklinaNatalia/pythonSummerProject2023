import openpyxl
wb  = openpyxl.load_workbook("../../Texts/text_08.xlsx")
ws = wb["Лист1"]
ws.append({5:12345, 6:123456})
ws.append([123, 234, 345, 456, 567, 678, 789, 890, 901])
wb.save("../../Texts/text_08.xlsx")