import asyncio
from aiohttp import ClientSession, ClientError
import pandas as pd
import time
import logging
from data_scrapping.main_logic_scrapper import scrape_data
from utils.search_strings import generate_search_strings


async def scrape_data_main(config):
    """This function extracts all data from the config file in respective lists,
       creates search strings, calls the scrape_data function for each search engine and search string,
       and calls the save_to_csv function to save the list of scraped data to a CSV file.

    Args:
        config (dict): Contains all the data provided by the user
    """

    try:
        # Get the values from the config file
        company_names = config["company_names"]
        keywords = config["keywords"]
        pages = config["pages"]
        selected_engines = config["search_engines"]

        # Call generate search string function to form search strings using data from the config
        search_strings = generate_search_strings(company_names, keywords)

        # List to store tasks for scraping
        tasks = []

        # Create an asynchronous session
        async with ClientSession() as session:
            # Loop through the list of search engines
            for engine in selected_engines:
                # Loop through the list of search strings
                for string in search_strings:
                    # Calling the scrape_data function for each asynchronous task
                    tasks.append(scrape_data(session, engine, string, pages))

            # Executing all tasks and gathering their results
            try:
                results = await asyncio.gather(*tasks)
            except Exception as e:
                logging.error(f"Error occurred while scraping data: {e}")
                return

        # Storing results in the output list
        output = []
        for subresult in results:
            for lists in subresult:
                output.append(lists)

        # Call the function to save the scraped data to a CSV file
        save_to_csv(output)

    except KeyError as e:
        logging.error(f"Missing key in config: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def save_to_csv(data):
    """Converts the list of scraped data into a CSV file and saves it for each different data.

    Args:
        data (list): List of scraped data
    """
    try:
        # Using pandas to convert list into dataframe
        output_df = pd.DataFrame(data)

        # Saving the CSV file to the provided path
        output_df.to_csv(f'./tasks_download/output_{int(time.time())}.csv', index=False, encoding='utf-8')
        logging.info(f"Data saved to 'output_{int(time.time())}.csv'")

    except Exception as e:
        logging.error(f"Error saving data to CSV: {e}")
