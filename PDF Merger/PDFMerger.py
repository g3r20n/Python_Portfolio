from PyPDF2 import PdfMerger, PdfFileReader

merger = PdfMerger()

pdf_files = ["PDFMerger/pdf_files/one.pdf", "PDFMerger/pdf_files/two.pdf"]

for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.write("merged_2_pages.pdf")
merger.close()