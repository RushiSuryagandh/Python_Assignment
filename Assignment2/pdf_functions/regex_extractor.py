import time
import re

def extract_data_from_regx(text):
    """ create different regex function to get fifferent values

    Args:
        text (string): pdf text used to extract the information.
    """
    email_pattern=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}'
    cin_number_pattern=r'[A-Z]{1}[0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}'
    mobile_number_pattern=r'\b(?:\d{3,5}[\s-]?)?[\d]{7,10}\b'
    pan_number_pattern=r'[A-Z]{5}[0-9]{4}[A-Z]{1}'
    dates_pattern=r'\b\d{2}/\d{2}/\d{4}\b'
    website_pattern=r'\bhttps?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?\b|\bwww\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?'
    
    # extracted data stored in file
    emails = re.findall(email_pattern, text)
    cin_numbers = re.findall(cin_number_pattern, text)
    mobile_numbers = re.findall(mobile_number_pattern, text)
    pan_numbers = re.findall(pan_number_pattern, text)
    dates = re.findall(dates_pattern, text)
    websites = re.findall(website_pattern, text)

    # print(emails,cin_numbers,mobile_numbers,pan_numbers,dates,websites)
    data = []
    for i in range(max(len(emails), len(cin_numbers), len(mobile_numbers), len(pan_numbers), len(dates), len(websites))):
        data_row = {
            'Email': emails[i] if i < len(emails) else '',
            'CIN': cin_numbers[i] if i < len(cin_numbers) else '',
            'Mobile Number': mobile_numbers[i] if i < len(mobile_numbers) else '',
            'PAN': pan_numbers[i] if i < len(pan_numbers) else '',
            'Date': dates[i] if i < len(dates) else '',
            'Website': websites[i] if i < len(websites) else ''
        }
        data.append(data_row)
    time.sleep(2)
    return data