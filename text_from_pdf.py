"""
install a python library called PyPDF2
"""

import PyPDF2
pdf = open("resume.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
no_pages = reader.numPages
print(no_pages)
page = reader.getPage(0)
print(page.extractText())
pdf.close()