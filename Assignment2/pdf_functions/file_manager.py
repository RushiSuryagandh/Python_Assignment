import os

def fetch_pdf_files(directory_path):
    pdf_files = []
    
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path):
            print(f"Error: The directory '{directory_path}' does not exist.")
            return pdf_files

        # Walk through the directory
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # Check if the file ends with ".pdf"
                if file.endswith('.pdf'):
                    try:
                        # Append the full file path to the list
                        pdf_files.append(os.path.join(root, file))
                    except Exception as e:
                        print(f"Error processing file '{file}': {e}")

    except PermissionError:
        print(f"Error: You don't have permission to access the directory '{directory_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred while accessing the directory '{directory_path}': {e}")

    return pdf_files
