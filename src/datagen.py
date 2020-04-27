'''
@brief 
This script reads cleaned bulldozer data and analyzes it to generate fake bulldozer failure data

@author David Hill, Jr.
'''
import datetime
import csv 
import random

def main():
    filename = '../data/clean/CLEANED_DOZER_DATA_1588016784.097396.csv'
    
    clean_file = csv.DictReader(open(filename, mode='r'))
    dataset = []
    for row in clean_file:
        dataset.append(row)
    
    print(GetGlobalWkhrMin(dataset))
    print(GetGlobalWkhrMax(dataset))
    print(GetGlobalPriceMax(dataset))
    print(GetGlobalPriceMin(dataset))

    

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


def GetPriceRange(minwkhr, maxwkhr):
    return





if __name__ == "__main__":
    main()
