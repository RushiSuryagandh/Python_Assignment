from bs4 import BeautifulSoup
import aiohttp
import asyncio
import time
import logging
import os

logging.basicConfig(filename="./scraping.log",
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    filemode='w',
                    level=logging.INFO)

async def fetch_data_from_article_async(session, url, title_tag, title_class, body_tag, body_class):
    """
    Asynchronously fetches the title and body content of an article from a given URL.
    Args:
        session (aiohttp.ClientSession): The aiohttp session used for making the HTTP request.
        url (str): The URL of the article to scrape.
        title_tag (str): The HTML tag to find the article title.
        title_class (str): The class of the tag that holds the article title.
        body_tag (str): The HTML tag that contains the body of the article.
        body_class (str): The class of the body tag that holds the article's body content.
    Returns:
        tuple: The title and body text of the article, or (None, None) if an error occurs.
    """
    try:
        async with session.get(url) as response:
            logging.info(f'fetching data for url {url}')
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            
            title = soup.find(title_tag, class_=title_class).text.strip()
            body = soup.find(body_tag, class_=body_class)
            body_content = body.find_all('p')
            
            body_text = ''
            for content in body_content:
                body_text += content.text.strip()
            
            return title, body_text
        logging.info('data feteches successfully')
    except Exception as e:
        print(f'Error fetching article from {url}: {e}')
        return None, None

async def scrape_media_async(site_name, config):
    """
    Scrapes the media content of a given site asynchronously based on the configuration.
    Args:
        site_name (str): The name of the site to scrape (e.g., "IndianExpress", "TheHindu").
        config (dict): The configuration dictionary containing site-specific details like URL, title tag, and body tag.
    Returns:
        None
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
    
    async with aiohttp.ClientSession() as session:
        title, body = await fetch_data_from_article_async(session, url, title_tag, title_class, body_tag, body_class)
        
        if title and body:
            filename = f"scrape_{site_name}.md"
            await save_to_markdown_async(title, body, filename,folder_path='./md_with_async')


def save_to_markdown_async(title, body,filename,folder_path):
    """Asynchronously saves the scraped article title and body content into a markdown file.
    Args:
        title (str): The title of the article.
        body (str): The body text of the article.
        folder_path (str): The path of the folder where the file will be saved.
        filename (str): The name of the markdown file where the content will be saved.
    Returns:
        None: This function does not return any value. It simply saves the content to a file.
    """
    try:
        # Create the folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Build the full path for the file
        file_path = os.path.join(folder_path, filename)

        # Save the content to the markdown file
        with open(file_path, 'w', encoding='utf-8') as file:
           file.write(f'# {title}\n\n{body}\n')

        print(f'File saved successfully in {file_path}')
        logging.info('File saved successfully')
    except Exception as e:
        logging.error(f'Error saving to {file_path}: {e}')


async def async_scrape(config):
    """
    asynchronous scraping of multiple media sites.
    Args:
        config (dict): The configuration data for all the websites to scrape.
    Returns:
        None
    """
    start_time = time.time()
    
    # Scraping both IndianExpress and TheHindu asynchronously
    await asyncio.gather(
        scrape_media_async("IndianExpress", config),
        scrape_media_async("TheHindu", config)
    )
    
    end_time = time.time()
    print(f"Async/Await execution time: {end_time - start_time} seconds")




