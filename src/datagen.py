'''
@brief 
This script reads cleaned bulldozer data and analyzes it to generate fake bulldozer failure data

@author David Hill, Jr.
'''
import csv 
import random

def main():
    print("""
    (                                            
    )\ )            )        (                   
    (()/(      )  ( /(    )   )\ )      (         
    /(_))  ( /(  )\())( /(  (()/(     ))\  (     
    (_))_   )(_))(_))/ )(_))  /(_))_  /((_) )\ )  
    |   \ ((_)_ | |_ ((_)_  (_)) __|(_))  _(_/(  
    | |) |/ _` ||  _|/ _` |   | (_ |/ -_)| ' \)) 
    |___/ \__,_| \__|\__,_|    \___|\___||_||_|  
                                              
    """)
    filename = '../data/clean/CLEANED_DOZER_DATA.csv'
    
    clean_file = csv.DictReader(open(filename, mode='r'))
    dataset = []
    for row in clean_file:
        dataset.append(row)

    print("=================================================RUNNING=====================================================")
    new_data = GenerateData(10000, dataset)

    heading = ['Name', 'WorkHrs', "Ask_Price"]

    outfile = "../data/generated/GENERATED_DOZER_DATA"".csv"
    
    with open(outfile, 'w') as csvfile: 

        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = heading) 
        
        # writing headers (field names) 
        writer.writeheader() 
        
        # writing data rows 
        writer.writerows(new_data) 
    print("[DONE]")


    

def GetGlobalWkhrMin(dataset):
    first = dataset[0]['WorkHrs'].replace(' hrs', '')
    first = int(first.replace(',', ''))
    wkhrmin = first
    for row in dataset:
        wkhrs = row['WorkHrs'].replace(' hrs', '')
        wkhrs = int(wkhrs.replace(',', ''))
        if wkhrs < wkhrmin:
            wkhrmin = wkhrs
    return wkhrmin

def GetGlobalWkhrMax(dataset):
    first = dataset[0]['WorkHrs'].replace(' hrs', '')
    first = int(first.replace(',', ''))
    wkhrmax = first
    for row in dataset:
        wkhrs = row['WorkHrs'].replace(' hrs', '')
        wkhrs = int(wkhrs.replace(',', ''))
        if wkhrs > wkhrmax:
            wkhrmax = wkhrs
    return wkhrmax
    
def GetGlobalPriceMax(dataset):
    first = dataset[0]['Ask_Price'].replace('US $', '')
    first = int(first.replace(',', ''))
    pricemax = first
    for row in dataset:
        price = row['Ask_Price'].replace('US $', '')
        price = int(price.replace(',', ''))
        if price > pricemax:
            pricemax = price
    return pricemax

def GetGlobalPriceMin(dataset):
    first = dataset[0]['Ask_Price'].replace('US $', '')
    first = int(first.replace(',', ''))
    pricemin = first
    for row in dataset:
        price = row['Ask_Price'].replace('US $', '')
        price = int(price.replace(',', ''))
        if price < pricemin:
            pricemin = price
    return pricemin


def GetPriceRange(minwkhr, maxwkhr, dataset):
    subset = []
    for row in dataset:
        wkhrs = row['WorkHrs'].replace(' hrs', '')
        wkhrs = int(wkhrs.replace(',', ''))
        if(wkhrs >= minwkhr and wkhrs <= maxwkhr):
            subset.append(row)
    
    return (GetGlobalPriceMin(subset), GetGlobalPriceMax(subset))

def GenerateData(size, dataset):
    new_data = []
    for i in range(size):
        line = {}
        line['Name'] = 'crawler_' + str(i)

        maxwkhrs = GetGlobalWkhrMax(dataset)
        minwkhrs = GetGlobalWkhrMin(dataset)
       
        new_machine_wkhrs = random.randrange(minwkhrs, maxwkhrs)
        
        line['WorkHrs'] = new_machine_wkhrs

        if(new_machine_wkhrs >= 100 and new_machine_wkhrs <= 3000):
            price_range = GetPriceRange(100, 3000, dataset)
            new_machine_price = random.randrange(price_range[0], price_range[1])
            line['Ask_Price'] = new_machine_price
            new_data.append(line)

        if(new_machine_wkhrs >= 3000 and new_machine_wkhrs <= 6000):
            price_range = GetPriceRange(3000, 6000, dataset)
            new_machine_price = random.randrange(price_range[0], price_range[1])
            line['Ask_Price'] = new_machine_price
            new_data.append(line)

        if(new_machine_wkhrs >= 6000 and new_machine_wkhrs <= 9000):
            price_range = GetPriceRange(6000, 9000, dataset)
            new_machine_price = random.randrange(price_range[0], price_range[1])
            line['Ask_Price'] = new_machine_price
            new_data.append(line)

        if(new_machine_wkhrs >= 9000 and new_machine_wkhrs <= 12000):
            price_range = GetPriceRange(9000, 12000, dataset)
            new_machine_price = random.randrange(price_range[0], price_range[1])
            line['Ask_Price'] = new_machine_price
            new_data.append(line)

        print("Entries generated: ", i, end="\r")
    return new_data
    





if __name__ == "__main__":
    main()
