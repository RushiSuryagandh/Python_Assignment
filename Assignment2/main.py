import time
from pdf_functions.config_manager import load_json
from pdf_functions.downloader import downlod_pdf
from pdf_functions.file_manager import fetch_pdf_files
from pdf_functions.pdf_extractor import extract_data_from_pdf
from pdf_functions.regex_extractor import extract_data_from_regx
from pdf_functions.csv_saver import save_to_csv
from decorators.execution_time import execution_time

@execution_time
def main():
    config =load_json()
    # loading jason file
    urls_data = config['urls']
    download_dir=config['directory_path']

    # download each file
    downlod_pdf(urls_data,download_dir)

    # Adding delay to avoid download of temp files instead of complete pdf
    time.sleep(2)

    #  Fetch the PDF file paths
    pdf_file_paths = fetch_pdf_files(download_dir)

    # Extract data from PDFs
    text = extract_data_from_pdf(pdf_file_paths)
    # Extract data using regex
    data = extract_data_from_regx(text)
    # Save to CSV
    save_to_csv(data)

    
if __name__=="__main__":
    main()