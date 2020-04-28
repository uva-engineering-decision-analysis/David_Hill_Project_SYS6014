from bs4 import BeautifulSoup
import urllib3
import time
import json
import datetime
import csv
import os
from stat import S_IREAD, S_IRGRP, S_IROTH

'''
This script pulls data from ironplanet.com a used bulldozer listing site. From the scraped data it generated a read-only 
csv file.
'''
def main():

    http = urllib3.PoolManager()

    urllib3.disable_warnings()

    print("""
    ___                    __                                
   /   \___ _______ _ __  / _\ ___ _ __ __ _ _ __   ___ _ __ 
  / /\ / _ \_  / _ \ '__| \ \ / __| '__/ _` | '_ \ / _ \ '__|
 / /_// (_) / /  __/ |    _\ \ (__| | | (_| | |_) |  __/ |   
/___,' \___/___\___|_|    \__/\___|_|  \__,_| .__/ \___|_|   
                                            |_|              
                                                                                                                                                                          
    """)

    links = ['https://www.ironplanet.com/Crawler+Dozers',
    'https://www.ironplanet.com/Crawler+Dozers#pstart=60&sm=0&c=1&mf=1',
    'https://www.ironplanet.com/Crawler+Dozers#pstart=120&sm=0&c=1&mf=1',
    'https://www.ironplanet.com/Crawler+Dozers#pstart=180&sm=0&c=1&mf=1',
    ]

    heading = ['Name', 'WorkHrs', "Ask_Price"]
    database = []

    # Crawls each link and pulls bulldozer data, stores into list
    PageCrawler(links, database)

    
    filename = "../data/raw/RAW_DOZER_DATA" + ".csv"

    with open(filename, 'w') as csvfile: 

        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = heading) 
        
        # writing headers (field names) 
        writer.writeheader() 
        
        # writing data rows 
        writer.writerows(database) 

    # Make file Read-Only
    os.chmod(filename, S_IREAD|S_IRGRP|S_IROTH)


       
        
def PageCrawler(links, database):
    print("=================================================RUNNING=====================================================")

    http = urllib3.PoolManager()  
    bulldozers_collected = 0

    for link in links:

        page = http.request('GET', link)
        soup = BeautifulSoup(page.data, 'html.parser')

        detail_items = soup.find_all(class_='sr_grid_details')

        for item in detail_items:

            line = {}

            bulldozers_collected += 1

            name = item.find("div", class_="sr_equip_desc")
            name = name.span.get_text()

            line['Name'] = name

            wkhrs = item.find("div", class_="sr_meter")

            if wkhrs.span:
                wkhrs = wkhrs.span.get_text()
            else:
                wkhrs = "None"
            
            line['WorkHrs'] = wkhrs
            
            price = item.find("div", class_="sr_price")

            if price.span:
                price = price.span.get_text()
            else:
                price = "None"

            line['Ask_Price'] = price

            # store collected data
            database.append(line)
            
            print("Items scraped: ", bulldozers_collected, end="\r")
    print("\n[DONE]")



if __name__ == "__main__":
    main()