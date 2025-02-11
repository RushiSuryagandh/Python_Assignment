import logging
from bs4 import BeautifulSoup

async def scrape_data(session, search_engine, search_string, pages):
    """This function scraps data from  search engines and search strings

    Args:
        session (CLientSession): aiohttp session
        search_engine (String): Search engine from which data is to be scrapped
        search_string (String)): Search string for which data is to be scrapped
        pages (integer): Number pages from which data is to be scrapped

    Returns:
        list: returns list of scrapped data
    """
    
    logging.info(f"Scrapping data from {search_engine} search engine for {search_string} search string")

    # using user agents to avoid blocking from websites
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Dictionary of search engines and there respective urls 
    search_engine_urls = {
        "google": "https://news.google.com/search?q=[yourquery]&tbm=nws",
        "yahoo": "https://news.search.yahoo.com/search?p=[yourquery]&b=[page]",
        "bing": "https://www.bing.com/news/search?q=[yourquery]&first=[page]"
    }

    # list where scrapped data will be saved
    data = []

    try:

        # if search engine is google this part will execute
        if search_engine == "google":

            # replacing the yourquery part from url with search string
            url = search_engine_urls["google"].replace("[yourquery]", search_string)
            async with session.get(url, headers=headers) as response:

                # handling the error if website does not work
                if response.status != 200:
                    logging.warning(f"Google link not working for {search_string}")
                    return []

                text = await response.text()
                soup = BeautifulSoup(text, "html.parser")
                articles = soup.find_all('article', {'class': 'IFHyqb DeXSAc'})
                
                for article in articles[:pages * 10]:
                    publisher = article.find('div', {'class': 'vr1PYe'}).text
                    link = article.find('a', {'class': 'WwrzSb'})['href']
                    title = article.find('a', {'class': 'JtKRv'}).text
                    date= article.find('time', {'class': 'hvbAAd'})['datetime'].split('T')[0]
                    
                    # adding the scraped data in our data list
                    data.append({
                        "Search_Engine": "Google",
                        "Search_String": search_string,
                        "Publisher": publisher,
                        "Title": title,
                        "Link": link,
                        "Date": date,
                    })

        # if search engine is yahoo this part will execute
        elif search_engine == "yahoo":
            
            # looping through number of pages provided by user
            for page in range(1, pages + 1):
                # formula to change pages in url
                page_no = str(page * 10 - 9)
                url = search_engine_urls["yahoo"].replace('[yourquery]', search_string).replace('[page]', page_no)
                async with session.get(url, headers=headers) as response:

                    # handling the error if website does not work
                    if response.status != 200:
                        logging.warning(f"Yahoo link not working for {search_string}")
                        return []

                    text = await response.text()
                    soup = BeautifulSoup(text, "html.parser")
                    articles = soup.find_all('div', {'class': 'dd NewsArticle'})
                    # looping through articles for the url
                    for article in articles:
                        publisher = article.find('span', {'class': 's-source fw-l'}).text
                        link_div = article.find('h4', {'class': 's-title fz-20 lh-m fw-500 ls-027 mt-8 mb-2'})
                        link = link_div.find('a')['href']
                        title = article.find('h4', {'class': 's-title fz-20 lh-m fw-500 ls-027 mt-8 mb-2'}).text
                        date_time = article.find('span', class_='s-time fz-14 lh-18 fc-dustygray fl-l mr-4').text.strip()
                        

                        # adding scraped data in our data list 
                        data.append({
                            "Search_Engine": "Yahoo",
                            "Search_String": search_string,
                            "Publisher": publisher,
                            "Title": title,
                            "Link": link,
                            "Date": date_time,
                            
                        })

        # if search engine is bing this part will execute
        elif search_engine == "bing":
            for page in range(1, pages + 1):
                # formula to change pages in url
                page_no = str(page * 10 - 9)
                url = search_engine_urls["bing"].replace('[yourquery]', search_string).replace('[page]', page_no)
                async with session.get(url, headers=headers) as response:

                # handling the error if website does not work
                    if response.status != 200:
                        logging.warning(f"Bing link not working for {search_string}")
                        return []

                    text = await response.text()
                    soup = BeautifulSoup(text, "html.parser")

                    # looping through articles till user provided number of pages as 1 page contains 10 links
                    articles = soup.find_all('div', {'class': 'news-card newsitem cardcommon'})
                    
                    for article in articles:
                        link = article.find('a', {'class': 'title'})['href']
                        publisher = article['data-author']
                        title = article.find('a', {'class': 'title'}).text
                        date_time = article.find('span', {'aria-label': True})['aria-label']
                        


                        # adding scraped data in our list of data
                        data.append({
                            "Search_Engine": "Bing",
                            "Search_String": search_string,
                            "Publisher": publisher,
                            "Title": title,
                            "Link": link,
                            "Date": date_time,
                            
                        })

        logging.info(f"Completed scraping data for {search_engine} search engine and {search_string} search string")

    except Exception as e:
        logging.error(f"An error occurred while scraping data from {search_engine} for {search_string}: {e}")

    return data