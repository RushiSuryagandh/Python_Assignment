import requests
from bs4 import BeautifulSoup
import logging
import os

def fetch_data_from_article(url, title_tag, title_class, body_tag, body_class):
    """
    Fetches article data from the provided URL and parses the content using BeautifulSoup.

    Args:
        url (str): The URL of the article to scrape.
        title_tag (str): The HTML tag used to define the article title.
        title_class (str): The class name associated with the title tag.
        body_tag (str): The HTML tag that contains the main content of the article.
        body_class (str): The class name associated with the body tag.

    Returns:
        tuple: A tuple containing the title (str) and body text (str) of the article.
               Returns (None, None) in case of an error.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
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


def save_to_markdown(title, body,filename,folder_path):
    """
    Saves the article title and body to a markdown file in a specific folder.

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
    
    except Exception as e:
        logging.error(f'Error saving to {file_path}: {e}')
