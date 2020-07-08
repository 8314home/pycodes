import PyPDF2

pdf_1 = PyPDF2.PdfFileReader(open('src/combined_pdf.pdf', 'rb'))
pdf_2 = PyPDF2.PdfFileReader(open('src/rotated_page_pdf.pdf', 'rb'))
writer_pdf = PyPDF2.PdfFileWriter()

wtr_mark = pdf_2.getPage(0)

for i_page in range(pdf_1.getNumPages()):
    pg = pdf_1.getPage(i_page)
    pg.mergePage(wtr_mark)
    writer_pdf.addPage(pg)
writer_pdf.write(open('src/watermarked_pdf.pdf', 'wb'))





