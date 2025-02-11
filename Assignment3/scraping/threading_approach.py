import threading
import time
from scraping.fetcher import fetch_data_from_article, save_to_markdown
import logging

def scrape_media_threaded(site_name, config):
    """
    Scrape media content using threading by fetching data and saving it to a markdown file.

    Args:
        site_name (str): The name of the site to scrape (e.g., "IndianExpress", "TheHindu").
        config (dict): A configuration dictionary that contains the site's URL and HTML parsing details.

    Returns:
        None: This function doesn't return any value. It fetches the article data and saves it to a markdown file.
    """
    logging.info('scrape media content')
    if site_name not in config:
        print(f"Configuration for {site_name} not found.")
        return

    site_config = config[site_name]
    url = site_config['url']
    title_tag = site_config['title_tag']
    title_class = site_config['title_class']
    body_tag = site_config['body_tag']
    body_class = site_config['body_class']
    
    title, body = fetch_data_from_article(url, title_tag, title_class, body_tag, body_class)
    
    if title and body:
        filename = f"scrape_{site_name}.md"
        save_to_markdown(title, body, filename,folder_path='./md_with_multithreading')

def threading_scrape(config):
    """
    Run the scraping tasks using multithreading for concurrent data fetching and saving.

    Args:
        config (dict): A configuration dictionary containing site details for scraping.

    Returns:
        None: This function doesn't return any value. It initiates the scraping tasks using multithreading.
    """
    start_time = time.time()
    
    # Create threads for scraping each site concurrently
    thread1 = threading.Thread(target=scrape_media_threaded, args=("IndianExpress", config))
    thread2 = threading.Thread(target=scrape_media_threaded, args=("TheHindu", config))
    
    # Start the threads
    thread1.start()
    thread2.start()
    
    # Wait for both threads to finish
    thread1.join()
    thread2.join()
    
    end_time = time.time()
    print(f"Multithreading execution time: {end_time - start_time} seconds")
