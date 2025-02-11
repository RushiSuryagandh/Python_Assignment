from multiprocessing import Process
import time
from scraping.fetcher import fetch_data_from_article, save_to_markdown

def scrape_media_multiprocess(site_name, config):
    """
    Scrape media content using multiprocessing by fetching data and saving it to a markdown file.

    Args:
        site_name (str): The name of the site to scrape (e.g., "IndianExpress", "TheHindu").
        config (dict): A configuration dictionary that contains the site's URL and HTML parsing details.

    Returns:
        None: This function doesn't return any value. It saves the fetched data to a markdown file.
    """
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
        save_to_markdown(title, body, filename,folder_path='./md_with_multiprocess')

def multiprocessing_scrape(config):
    """
    Run the scraping tasks using multiprocessing for concurrent data fetching and saving.

    Args:
        config (dict): A configuration dictionary containing site details for scraping.

    Returns:
        None: This function doesn't return any value. It runs the scraping tasks using multiprocessing.
    """
    start_time = time.time()
    
    # Create processes for scraping each site concurrently
    process1 = Process(target=scrape_media_multiprocess, args=("IndianExpress", config))
    process2 = Process(target=scrape_media_multiprocess, args=("TheHindu", config))
    
    # Start the processes
    process1.start()
    process2.start()
    
    # Wait for both processes to finish
    process1.join()
    process2.join()
    
    end_time = time.time()
    print(f"Multiprocessing execution time: {end_time - start_time} seconds")
