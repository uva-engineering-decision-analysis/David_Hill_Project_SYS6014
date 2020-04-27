'''
@brief 
This script reads raw, scraped csv bulldozer data and cleans it. It then saves the data in a new file in the
clean folder.

@author David Hill, Jr.
'''
# importing the csv module 
import csv 
import random
import os
from stat import S_IREAD, S_IRGRP, S_IROTH
  
def main():

    print("""
    ______      _          _____ _                            
    |  _  \    | |        /  __ \ |                           
    | | | |__ _| |_ __ _  | /  \/ | ___  __ _ _ __   ___ _ __ 
    | | | / _` | __/ _` | | |   | |/ _ \/ _` | '_ \ / _ \ '__|
    | |/ / (_| | || (_| | | \__/\ |  __/ (_| | | | |  __/ |   
    |___/ \__,_|\__\__,_|  \____/_|\___|\__,_|_| |_|\___|_|   
                                                                    
        """)

    filename = '../data/raw/RAW_DOZER_DATA.csv'
    clean_data = []
    raw_file = csv.DictReader(open(filename, mode='r'))
    print("=================================================RUNNING=====================================================")
    for row in raw_file:
        additem = True
        if("US" not in row["Ask_Price"]):
            additem = False
        if(row["WorkHrs"] == 'None' or row["WorkHrs"] =='See Report'):
            additem = False
        if(additem):
            clean_data.append(row)

    outfile = "../data/clean/CLEANED_DOZER_DATA" + ".csv"

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
    print("[DONE]")

if __name__ == "__main__":
    main()