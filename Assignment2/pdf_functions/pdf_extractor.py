import PyPDF2
import time

def extract_data_from_pdf(pdf_file_paths):
    text = ''
    for pdf in pdf_file_paths:
        with open(pdf, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            time.sleep(2)  # Simulating processing time

            # Extract text from the first 4 pages (if available)
            for page_num in range(min(4, len(pdf_reader.pages))):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
    
    return text
