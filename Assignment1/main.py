# importing required libraries
import asyncio
import logging
from config.config_func import load_config
from data_scrapping.scrapper import scrape_data_main

# Main
if __name__ == "__main__":
    # Adding logging
    logging.basicConfig(
        filename='logging_details.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w'
    )
    
    try:
        logging.info("Starting program")
    
        config = load_config() # Loading the confif.json file
        if config:
                asyncio.run(scrape_data_main(config)) # Scraping data from loaded config file
        print('Succefully Done')
        
    except Exception as e:
        print(f"Error occured in main loop : {e}") # Handling exception