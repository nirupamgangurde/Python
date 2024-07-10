from PyPDF2 import PdfFileMerger
import os

merger = PdfFileMerger()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    with open(pdf, 'rb') as file:
        merger.append(file)

merger.write("merged.pdf")
merger.close()
