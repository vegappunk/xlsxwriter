import xlsxwriter
workbook = xlsxwriter.Workbook('2321321321.xlsx')
worksheet = workbook.add_worksheet()
# данные
expenses = (  
    ["79840000000", "Тест", "Тест", "Тест", "2020-07-08 00:59:36", "Отбор проектов Бердигестяхского наслега ППМИ", "лесная 14", "2020-10-27 22:51:59"],
    ["79840000000", "Тест", "Тест", "Тест", "2020-10-28 20:28:47", "Просим Вас указать в каком объеме, по Вашему мнению, можете участвовать в софинансировании проектов ППМИ", "200", "2020-10-28 20:30:05"],
)

for i, (phone, name, sur, pat, userTime, desc, title, voiceTime) in enumerate(expenses, start=1):
    worksheet.write(f'A{i}', phone)
    worksheet.write(f'B{i}', name)
    worksheet.write(f'C{i}', sur)
    worksheet.write(f'D{i}', pat)
    worksheet.write(f'E{i}', userTime)
    worksheet.write(f'F{i}', desc)
    worksheet.write(f'G{i}', title)
    worksheet.write(f'H{i}', voiceTime)
# сохраняем и закрываем
workbook.close()
