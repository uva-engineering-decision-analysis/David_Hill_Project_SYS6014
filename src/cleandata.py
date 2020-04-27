'''
@brief 
This script reads raw, scraped csv bulldozer data and cleans it. It then saves the data in a new file in the
clean folder.

@author David Hill, Jr.
'''
# importing the csv module 
import datetime
import csv 
import random
import os
from stat import S_IREAD, S_IRGRP, S_IROTH
  
def main():

    filename = '../data/raw/USED_DOZER_DATA_1588016153.631536.csv'
    clean_data = []
    raw_file = csv.DictReader(open(filename, mode='r'))

    for row in raw_file:
        additem = True
        if("US" not in row["Ask_Price"]):
            additem = False
        if(row["WorkHrs"] == 'None' or row["WorkHrs"] =='See Report'):
            additem = False
        if(additem):
            clean_data.append(row)

    timestamp = str(datetime.datetime.now().timestamp())
    outfile = "../data/clean/CLEANED_DOZER_DATA_"+ timestamp +".csv"

    heading = ['Name', 'WorkHrs', "Ask_Price"]

    with open(outfile, 'w') as csvfile: 

        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = heading) 
        
        # writing headers (field names) 
        writer.writeheader() 
        
        # writing data rows 
        writer.writerows(clean_data) 
        
    # Make file Read-Only
    os.chmod(filename, S_IREAD|S_IRGRP|S_IROTH)


if __name__ == "__main__":
    main()