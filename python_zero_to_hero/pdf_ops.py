import PyPDF2

with open('src/original.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    # help(page)
    rotated_page = page.rotateClockwise(180)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(rotated_page)
    with open('src/rotated_page_pdf.pdf', 'wb') as new_file:
        writer.write(new_file)
