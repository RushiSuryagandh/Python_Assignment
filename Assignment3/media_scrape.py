import aiohttp
import asyncio
from bs4 import BeautifulSoup
import logging
import json

# Create and configure logger
logging.basicConfig(filename="./scraping.log",
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    filemode='w',
                    level=logging.INFO)

def load_config(filename="config.json"):
    """
    Loads the configuration from a JSON file.

    Args:
        filename (str): The path to the configuration file. Defaults to "config.json".
    
    Returns:
        dict: The configuration data loaded from the JSON file.
        None: If an error occurs while loading the config file.
    """
    try:
        with open(filename, 'r') as file:
            config = json.load(file)
        logging.info('Successfully open the json file')
        return config
    except Exception as e:
        logging.error(f"Error loading config file: {e}")
        return None

async def fetch_data_from_article(session, url, title_tag, title_class, body_tag, body_class):
    """
    Asynchronously fetches the title and body content of an article from the given URL.

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
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            
            title = soup.find(title_tag, class_=title_class).text.strip()
            body = soup.find(body_tag, class_=body_class)
            body_content = body.find_all('p')
            
            body_text = ''
            for content in body_content:
                body_text += content.text.strip()
            
            logging.info("Successfully fetched article.")
            return title, body_text
    except Exception as e:
        logging.error(f'Error fetching article from {url}: {e}')
        return None, None

async def save_to_markdown(title, body, filename):
    """
    Asynchronously saves the title and body content of the article to a markdown file.

    Args:
        title (str): The title of the article.
        body (str): The body content of the article.
        filename (str): The name of the file to save the content to.
    
    Returns:
        None
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'# {title}\n\n{body}\n')
        logging.info('File saved.')
        print(f'File Saved successfully in {filename}')
    except Exception as e:
        logging.error(f'Error saving to {filename}: {e}')

async def scrape_media(site_name, config):
    """
    Asynchronously scrapes a website's article data and saves it to a markdown file.

    Args:
        site_name (str): The name of the site to scrape (e.g., "IndianExpress", "TheHindu").
        config (dict): The configuration data containing URLs, tags, and classes for scraping.
    
    Returns:
        None
    """
    if site_name not in config:
        logging.error(f"Site configuration for {site_name} not found.")
        return
    
    site_config = config[site_name]
    
    url = site_config['url']
    title_tag = site_config['title_tag']
    title_class = site_config['title_class']
    body_tag = site_config['body_tag']
    body_class = site_config['body_class']
    
    async with aiohttp.ClientSession() as session:
        title, body = await fetch_data_from_article(session, url, title_tag, title_class, body_tag, body_class)
        
        if title and body:
            filename = f"scrape_{site_name}.md"
            await save_to_markdown(title, body, filename)

async def main():
    """
    Main function to run the program. Prompts the user for input and scrapes the requested websites 
    using async/await.

    Returns:
        None
    """
    # Load the config file
    config = load_config()
    
    if not config:
        print("Failed to load configuration.")
        return
    
    print('Enter Your Choice To Get The News Information:-')
    print("1. Indian Express\n2. The Hindu\n3. Both\n")
    
    choice = input("Enter your choice: ").strip()
    
    # Using async/await for simultaneous scraping
    match choice:
        case "1":
            # Scrape Indian Express asynchronously
            await scrape_media("IndianExpress", config)
        case "2":
            # Scrape The Hindu asynchronously
            await scrape_media("TheHindu", config)
        case "3":
            # Scrape both Indian Express and The Hindu asynchronously
            await asyncio.gather(
                scrape_media("IndianExpress", config),
                scrape_media("TheHindu", config)
            )
        case _:
            print("Invalid choice.")

if __name__ == '__main__':
    asyncio.run(main())
