import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def downlod_pdf(urls_data,download_dir):
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option('prefs',{
        'download.default_directory':'C:\\Users\\RushikeshSuryagandh\\PYTHON_ASSIGNMENT\\Assignment2\\download_pdf',  # Gives the directory path to store the pdf
        'download.prompt_for_download':False, # s/w doesn't ask user about confirmation of downloading 
        'plugins.always_open_pdf_externally':True # means that PDF files will always be opened in an external PDF viewer instead of within the software or browser itself.

    })
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    # This part uses a library called webdriver-manager to automatically download and manage the correct version of ChromeDriver (the Chrome browser’s WebDriver). don't have to manually download or specify the driver’s location.
    
    for url in urls_data: # for each url in urls_data
        # Extract the filename from the URL (or create a unique filename based on URL)
        file_name = url.split('/')[-1]
        file_path = os.path.join(download_dir, file_name)
        # Check if the file already exists
        print(os.listdir(download_dir))
        if not os.path.exists(file_path):
                        # If the file doesn't exist, download it
            driver.get(url)
        else:
            # If the file exists, skip downloading
            print(f"{file_name} already exists. Skipping download.")
    
