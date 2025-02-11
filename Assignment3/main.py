# main.py
from scraping.config_loader import load_config
from scraping.threading_approach import threading_scrape
from scraping.multiprocessing_approach import multiprocessing_scrape
from scraping.async_approach import async_scrape
import asyncio

def main():
    config = load_config()
    
    if not config:
        print("Failed to load configuration.")
        return
    
    print("\nStarting Multithreading...\n")
    threading_scrape(config)
    
    print("\nStarting Multiprocessing...\n")
    multiprocessing_scrape(config)
    
    print("\nStarting Async/Await...\n")
    asyncio.run(async_scrape(config))

if __name__ == '__main__':
    main()
