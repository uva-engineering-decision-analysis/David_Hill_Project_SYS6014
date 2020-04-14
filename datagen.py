
# importing the csv module 
import csv 
import random
  
# field names 
fields = ['Name', 'Age', 'Work-Hours', 'Value'] 
  
# data rows of csv file
rows = []

for i in range(1000):
    name = "Crawler_"+ str(i)
    age = random.randrange(1, 20)
    if(age < 5):
        work_hrs = random.randrange(500, 5000)
    elif(age > 5 and age < 10):
        work_hrs = random.randrange(500, 30000)
    elif(age > 10 and age < 15):
        work_hrs = random.randrange(500, 50000)
    else:
        work_hrs = random.randrange(500, 70000)

    if(work_hrs in range(500, 5000)):
        value = random.randrange(85000, 350000)

    elif(work_hrs in range(5000, 30000)):
        value = random.randrange(55000, 250000)

    elif(work_hrs in range(30000, 70000)):
        value = random.randrange(500, 15000)
    else:
        value = random.randrange(500, 2000)

    row = [name, age, work_hrs, value]

    rows.append(row)
    

# name of csv file 
filename = "./data/dozer_failures.csv"
  
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(rows)
