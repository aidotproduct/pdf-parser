from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    for index, image in enumerate(images):
        image.save(f'{pdf_path}-{index}.png')


def task():
    convert_pdf_to_images('/home/milind/Python/Documents/Capital_Gain_Stmt_PY_IP121098392 (002)_NOPASS.pdf')
    # convert_pdf_to_images('example-multipage.pdf')


if __name__ == "__main__":
    task()