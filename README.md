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
    ├── Assignment2/
    │   ├── config.json
    │   ├── main.py
    │   ├── requirements.txt
    │   ├── decorators/
    │   │   ├── __init__.py
    │   │   ├── execution_time.py
    │   │   └── __pycache__/
    │   ├── download_pdf/
    │   ├── output/
    │   │   └── pdf_results.csv
    │   └── pdf_functions/
    │       ├── __init__.py
    │       ├── config_manager.py
    │       ├── csv_saver.py
    │       ├── downloader.py
    │       ├── file_manager.py
    │       ├── pdf_extractor.py
    │       ├── regex_extractor.py
    │       └── __pycache__/
    └── Assignment3/
        ├── config.json
        ├── main.py
        ├── media_scrape.py
        ├── requirements.txt
        ├── md_with_async/
        │   ├── scrape_IndianExpress.md
        │   └── scrape_TheHindu.md
        ├── md_with_multiprocess/
        │   ├── scrape_IndianExpress.md
        │   └── scrape_TheHindu.md
        ├── md_with_multithreading/
        │   ├── scrape_IndianExpress.md
        │   └── scrape_TheHindu.md
        └── scraping/
            ├── __init__.py
            ├── async_approach.py
            ├── config_loader.py
            ├── fetcher.py
            ├── multiprocessing_approach.py
            ├── threading_approach.py
            └── __pycache__/
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

# Assignment 2

# PDF Data Extractor

A Python script that downloads PDF files from a list of URLs, extracts data from the PDFs using regular expressions, and saves the extracted data to a CSV file.

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/pdf-data-extractor.git
```

2. Navigate to the project directory:

```
cd pdf-data-extractor
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Create a `config.json` file in the `pdf_functions` directory with the following structure:

```json
{
  "urls": [
    "https://example.com/file1.pdf",
    "https://example.com/file2.pdf",
    "https://example.com/file3.pdf"
  ],
  "directory_path": "path/to/download/directory"
}
```

2. Replace the `urls` and `directory_path` values with your own data.

3. Run the script:

```
python main.py
```

The script will download the PDF files, extract data using regular expressions, and save the extracted data to a CSV file in the `directory_path` specified in the `config.json` file.

# Assignment 3
# Web Scraper

A powerful web scraping tool that utilizes multiple approaches to efficiently extract data from websites.

## Installation

To install the web scraper, follow these steps:

1. Clone the repository:
```
git clone https://github.com/your-username/web-scraper.git
```

2. Navigate to the project directory:
```
cd web-scraper
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

To use the web scraper, run the following command:

```
python main.py
```

This will execute the web scraping process using three different approaches: multithreading, multiprocessing, and asynchronous programming.







