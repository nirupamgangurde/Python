import PyPDF2
a = PyPDF2.PdfFileReader('Ml Cheatsheet.pdf')
str = ""
for i in range(1, 3):
    str += a.getPage(i).extractText()

with open("text.txt","w", encoding='utf-8') as f:
    f.write(str)