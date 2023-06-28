# Scraping Brands Info

Web scraping script.

## Description

This is a web scraper, which extract companies and their websites and exports the data into Excel Spreadsheet. 
Due to the high number of requests, I've added an option to use a proxy server.

## Dependencies

* Python 3, requests, pandas, BeautifulSoup4

## Executing/testing the program

1. You may add your own proxy or use the one I've included
2. At the end of the script there is an option to save the scraped data to .xlsx file
3. The execution takes time, so if you are testing the script you may change line 39 (number of brands to scrape on each page) and line 49 (number of pages to crawl). Check comments for more information
