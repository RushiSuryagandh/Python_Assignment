import os

def fetch_pdf_files(directory_path):
    pdf_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Check if the file ends with ".pdf"
            if file.endswith('.pdf'):
                # Append the full file path to the list
                pdf_files.append(os.path.join(root, file))
                
    # print(f"Found PDF: {pdf_files}") 
    return pdf_files