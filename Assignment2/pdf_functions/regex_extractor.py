import re

def extract_data_from_regx(text):
    """Create different regex functions to get different values and handle errors gracefully.

    Args:
        text (string): PDF text used to extract the information.
    """
    try:
        # Pre-compile regex patterns to optimize execution speed
        # used to recompile a regular expression with new source
        # flags after the RegExp object has already been created.
        email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}')
        cin_number_pattern = re.compile(r'[A-Z]{1}[0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}')
        mobile_number_pattern = re.compile(r'\b(?:\d{3,5}[\s-]?)?[\d]{7,10}\b')
        pan_number_pattern = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]{1}')
        dates_pattern =re.compile(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1[89]|2[01])([0-9]{2})')
        website_pattern = re.compile(r'\bhttps?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?\b|\bwww\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?')

        # Extract data using compiled regex patterns
        emails = email_pattern.findall(text)
        # print(emails)
        cin_numbers = cin_number_pattern.findall(text)
        mobile_numbers = mobile_number_pattern.findall(text)
        pan_numbers = pan_number_pattern.findall(text)

        # dates_pattern gives tuples of list

        # it finds all the dates list
        list_of_dates =dates_pattern.findall(text)

        # create a empty list to store the actual date
        dates = []
        for date in list_of_dates:
            formated_date = date[0] +"/"+ date[1] +"/"+  date[2] + date[3]
            dates.append(formated_date)
        
        websites = website_pattern.findall(text)

        # Get the maximum length of the lists to iterate over
        max_length = max(len(emails), len(cin_numbers), len(mobile_numbers), len(pan_numbers), len(dates), len(websites))

        # Use list comprehension and zip to combine lists efficiently
        data = [
            {
                'Email': emails[i] if i < len(emails) else '',
                'CIN': cin_numbers[i] if i < len(cin_numbers) else '',
                'Mobile Number': mobile_numbers[i] if i < len(mobile_numbers) else '',
                'PAN': pan_numbers[i] if i < len(pan_numbers) else '',
                'Date': dates[i] if i < len(dates) else '',
                'Website': websites[i] if i < len(websites) else ''
            }
            for i in range(max_length)
        ]
        
        return data
    
    except Exception as e:
        # Print error message if any exception occurs during the process
        print(f"An error occurred while extracting data: {e}")
        return []
