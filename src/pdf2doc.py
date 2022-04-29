from pdf2docx import Converter

pdf_file = "D:\\阿里云盘\\会计下册.pdf"
docx_file = "D:\\阿里云盘\\会计下册.docx"

# Convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
