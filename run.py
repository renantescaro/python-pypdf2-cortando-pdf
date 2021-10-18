from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject


pdf_reader = PdfFileReader(str('carro.pdf'))
first_page:PageObject = pdf_reader.getPage(0)

# x, y, width e height
print(first_page.mediaBox)


first_page.mediaBox.upperRight = (684, 466)
first_page.mediaBox.lowerLeft  = (159, 129) 


pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)
with Path("carro_cortado.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)