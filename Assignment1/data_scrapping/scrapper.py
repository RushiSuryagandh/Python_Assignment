# importing the required libraries
import asyncio
from aiohttp import ClientSession
import pandas as pd
import time
import logging
from data_scrapping.main_logic_scrapper import scrape_data
from utils.search_strings import  generate_search_strings



async def scrape_data_main(config):

    """This function  extracts all data from config file in respective lists,
       creates search strings, call the scrape_data function for each search engine and search string
       and call the save to csv function to save list of scraped data to a csv file

    Args:
        config (Dictionary): Contains all the data provided by user
    """

    # get the value from config file
    company_names = config["company_names"]
    keywords = config["keywords"]
    pages = config["pages"]
    selected_engines = config["search_engines"]

    # calling generate search string function to form search strings using data from json file
    search_strings = generate_search_strings(company_names,keywords)

    # list to strore tasks for scraping
    tasks = [] 
    # creating a asynchronous session
    async with ClientSession() as session:
        # looping through list of search engine
        for engine in selected_engines:
            # looping through list of search strings
            for string in search_strings:
                # calling the scrape_data function for each asynchronous task
                tasks.append(scrape_data(session, engine, string, pages))

        # executing all tasks and gathering there results
        results = await asyncio.gather(*tasks)

    # storing a result in output list
    output = []
    for subresult in results:
        for lists in subresult:
            output.append(lists)

    # calling function to save the scraped data to a CSV file
    save_to_csv(output)
    
def save_to_csv(data):
    """ Converts the list of scraped data in a csv file and saves it for each different data

    Args:
        data (list): list of scraped data
    """

    # using pandas to convert list into dataframe
    output_df = pd.DataFrame(data)
    # saving the csv file to provided path
    output_df.to_csv(f'./tasks_download/output_{int(time.time())}.csv')
    logging.info(f"Data saved to 'output_{int(time.time())}.csv")