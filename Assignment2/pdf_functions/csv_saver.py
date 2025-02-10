import pandas as pd

def save_to_csv(data, file_name='./output/pdf_results.csv'):
    """Saves extracted data to a CSV file.

    This function takes a list of dictionaries containing structured data (such as emails, CIN numbers, 
    mobile numbers, PAN numbers, dates, and websites), and writes the data to a CSV file.

    Args:
        data (list of dict): A list of dictionaries .
        file_name (str, optional): The path where the CSV file will be saved. 
            Defaults to './output/pdf_results.csv'.

    Returns:
        None

    Note:
        - The CSV file will be created or overwritten if it already exists
    """
    df = pd.DataFrame(data, columns=["Email", "CIN", "Mobile Number", "PAN", "Date", "Website"])
    df.to_csv(file_name, index=False, encoding='utf-8')
    print(f'Data successfully saved in {file_name}')
