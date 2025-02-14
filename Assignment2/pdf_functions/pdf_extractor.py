import PyPDF2
import time
import os

def extract_data_from_pdf(pdf_file_paths):
    text = ''
    for pdf in pdf_file_paths:
        try:

            with open(pdf, 'rb') as file:
                try:
                    # Initialize PDF reader
                    pdf_reader = PyPDF2.PdfReader(file)
                    time.sleep(2)  # Simulating processing time

                    # Extract text from the first 4 pages (if available)
                    for page_num in range(min(4, len(pdf_reader.pages))):
                        page = pdf_reader.pages[page_num]
                        text += page.extract_text()

                except PyPDF2.errors.PdfReadError as e:
                    print(f"Error reading PDF file '{pdf}': {e}")
                except Exception as e:
                    print(f"An error occurred while processing '{pdf}': {e}")
        
        except FileNotFoundError:
            print(f"Error: The file '{pdf}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred with the file '{pdf}': {e}")

    return text
