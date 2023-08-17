from PyPDF2 import PdfWriter
import os
from datetime import datetime


merger = PdfWriter()
pdfPath = 'C:\\Temp\\PDF\\'
pdfList = os.listdir(pdfPath)
print(pdfList)

currentDateTime = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
print(datetime.now())

for f in pdfList:
    if f.endswith('.pdf'):
        file = os.path.join(pdfPath, f)
        merger.append(file)
    else:
        continue

merger.write(f"{pdfPath}mergedpdf {currentDateTime}.pdf")
merger.close()
