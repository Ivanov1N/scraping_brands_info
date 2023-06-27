import requests
from bs4 import BeautifulSoup
import pandas as pd

""" Setting up a proxy server and headers information. I suggest using your own (if you have one) or another free proxy
"""
prox = {
    'https': '113.53.231.133:3129'
    }

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

companies = []

# Extracting company names
def extract(page):
    url = f'https://www.1800d2c.com/all-brands?0dc819aa_page={page}'
    req = requests.get(url, headers, proxies=prox)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup
    print (req.status_code)

# Extracting company website
def web_page_collect (href):
    url2 = f'https://www.1800d2c.com{href}'
    req2 = requests.get(url2, headers, proxies=prox)
    soup2 = BeautifulSoup(req2.content, 'html.parser')
    link_box = soup2.find('a', class_= 'bxl w-button', href = True)
    if link_box == None:
        link = ''   
    else:
        link = link_box.get('href')
    return link
    print (req2.status_code)

# Parsing each company name and website into a dictionary
def transform(soup):
    comp_list = soup.find_all('a', class_='cardlinkwrap w-inline-block', href=True)
    for i in comp_list:  # Each page contains approximately 100 companies. To test the script you may try with a couple, because it takes time.
        comp_name = i.text
        comp_page = web_page_collect (i['href'])
        company_info = {
            'Company Name': comp_name,
            'Webpage': comp_page
        }
        companies.append(company_info)

# Start scraping
for i in range (1, 14):  # The address contains a total of 14 pages. Again... if testing, try with a few pages
    transform(extract(i))

companies_table = pd.DataFrame(companies)

print (companies_table)

# An option to save the data as Excel table

#companies_table.to_excel ('Companies.xlsx')







