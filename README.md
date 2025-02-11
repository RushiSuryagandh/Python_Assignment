# Python_Assignment
```
### File Structure
Directory structure:
└── rushisuryagandh-python_assignment/
    ├── README.md
    ├── Assignment1/
    │   ├── main.py
    │   ├── requirements.txt
    │   ├── config/
    │   │   ├── __init__.py
    │   │   ├── config_func.py
    │   │   └── __pycache__/
    │   ├── data_scrapping/
    │   │   ├── __init__.py
    │   │   ├── main_logic_scrapper.py
    │   │   ├── scrapper.py
    │   │   └── __pycache__/
    │   ├── tasks_download/
    │   │   ├── config.json
    │   │   └── output_1739289490.csv
    │   └── utils/
    │       ├── __init__.py
    │       ├── search_strings.py
    │       └── __pycache__/
    
```

# Assignment 1
## Data Scraper

A Python-based data scraping tool that extracts data from various sources based on a configuration file.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/data-scraper.git
```

2. Navigate to the project directory:
```
cd data-scraper
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Create a `config.json` file in the `config` directory with the necessary configuration settings.

2. Run the main script:
```
python main.py
```



# Assignment 2 - PDF Processing

This project is designed to process PDFs, extract relevant data, and save the results in a structured format. It includes utilities for downloading, extracting, and managing PDF files.

## Project Structure

```
Assignment2/
│── config.json                # Configuration file
│── main.py                    # Main script
│── requirements.txt           # Dependencies
│
├── decorators/                 # Utility decorators
│   ├── __init__.py
│   ├── execution_time.py       # Measures execution time of functions
│
├── download_pdf/               # Sample PDFs for processing
│   ├── Draft-Annual-Return-FY-2021-22.pdf
│   ├── Form-MGT-7.pdf
│
├── output/                     # Output directory
│   ├── pdf_results.csv         # Extracted data results
│
├── pdf_functions/              # Core PDF processing functions
│   ├── __init__.py
│   ├── config_manager.py       # Handles configuration settings
│   ├── csv_saver.py            # Saves extracted data to CSV
│   ├── downloader.py           # Downloads PDFs
│   ├── file_manager.py         # Manages file operations
│   ├── pdf_extractor.py        # Extracts data from PDFs
│   ├── regex_extractor.py      # Performs regex-based text extraction
│
```

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the main script to start processing:
```sh
python main.py
```

## Configuration

Modify `config.json` to change settings such as input PDF paths, output directories, or extraction rules.

## Features

- **PDF Downloading**: Downloads PDFs from URLs.
- **Text Extraction**: Extracts text from PDFs using regex.
- **CSV Export**: Saves extracted data to a structured CSV file.
- **Execution Time Measurement**: Uses decorators to track function execution time.

# Assignment 3 - Web Scraping Project

## Project Overview
This project is designed for web scraping using different approaches such as:
- Asynchronous processing
- Multithreading
- Multiprocessing

## Folder Structure
```
Assignment3/
│── config.json                # Configuration file for scraping
│── main.py                    # Main script to run the project
│── media_scrape.py            # Script for media scraping
│── requirements.txt           # List of dependencies
│── scraping.log               # Log file for scraping activities
│── md_with_async/             # Contains implementation using async programming
│── md_with_multiprocess/      # Contains implementation using multiprocessing
│── md_with_multithreading/    # Contains implementation using multithreading
│── media_scrape/              # Directory for storing scraped media
│── scraping/                  # Directory for storing scraped data
```

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv media_scrape
   source media_scrape/bin/activate  # On Windows use `media_scrape\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt

## Usage
Run the main script:
```bash
python main.py
```

Modify `config.json` to customize scraping settings.

















