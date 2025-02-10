import fitz
import time

def extract_data_from_pdf(pdf_file_paths):
    text=''
    for pdf in pdf_file_paths:
        # print(pdf)
        open_pdf=fitz.open(pdf)
        time.sleep(2)

        # print(open_pdf)
        for page_num in range(4):
            text+=open_pdf[page_num].get_text('text')
        # print(text)
    return text