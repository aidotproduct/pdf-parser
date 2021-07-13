from PyPDF2 import PdfFileReader, PdfFileWriter

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file, \
    open(output_path, 'wb') as output_file:
    reader = PdfFileReader(input_file)
    reader.decrypt(password)

    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
      writer.addPage(reader.getPage(i))

    writer.write(output_file)

if __name__ == '__main__':
  # example usage:
  decrypt_pdf('/home/milind/Python/Documents/Capital_Gain_Stmt_PY_IP121098392 (002).pdf', '/home/milind/Python/Documents/Capital_Gain_Stmt_PY_IP121098392 (002)_NOPASS.pdf', 'AAYPC8552D')