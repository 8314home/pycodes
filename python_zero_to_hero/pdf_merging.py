import sys
import PyPDF2


def combine_pdf_list(pdf_list):
    mrg = PyPDF2.PdfFileMerger()
    for pdf_file in pdf_list:
        print(pdf_file)
        mrg.append(pdf_file)
    mrg.write('src/combined_pdf.pdf')


if __name__ == "__main__":
    input_list = sys.argv[1:]
    print(input_list)
    input_list = list(map(lambda x: 'src/' + x, input_list))
    print(input_list)
    combine_pdf_list(input_list)
