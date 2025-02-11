def generate_search_strings(company_name, keywords):
    """ This function generates all possible combinations of comapany names and keywords
       
    """
    search_string = []
    # looping through each company name and keyword to combine them
    for company in company_name:
        for keyword in keywords:
            search_string.append(company + " " + keyword)
    return search_string