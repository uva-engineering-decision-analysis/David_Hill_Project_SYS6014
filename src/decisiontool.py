'''
@brief 
This script reads generated bulldozer data and makes predictions as to when a bulldozer will 
experience catastrophic failure

@author David Hill, Jr.

@assumption This script is assuming the data reflects bulldozers that failed after 1584 work hours
@assumption The dataset reflects bulldozers that failed during average conditions
@assumption The amount of work hours in an average use case is 1584 which is derived by:
            22 working days a month x 9 months x 8 hours a day = 1584 work hours
'''

from scipy.stats import poisson
import csv 

def main():
    filename = '../data/generated/GENERATED_DOZER_DATA.csv'

    datafile = csv.DictReader(open(filename, mode='r'))
    dataset = []
    for row in datafile:
        dataset.append(row)
    
    workhours = int(input("Enter the amount of workhours on the machine: "))
    lifetime = int(input("Enter the amount work hours you expect to utilize the machine for: "))
    periods = int(input("How many work hours is acceptable until a failure: "))/1584
    
    # We expect 1 failure to happen
    failures = 1

    # Chance of failure during accaptable period
    lam_value_p = FailureRate(workhours, dataset) * periods
    prob_fail_periods = PoissonProb(failures, lam_value_p)

    # Chance of failure during lifetime ownership
    lifetime_periods = lifetime/1584
    lam_value_l = FailureRate(workhours, dataset) * lifetime_periods
    prob_fail_lifetime = PoissonProb(failures, lam_value_l)

    print("-------------------------------------------------------------------------------------")
    print("Report")
    print("-------------------------------------------------------------------------------------")
    print('Work-Hours on machine: ', workhours)
    print('Work-Hours Expected During Ownership: ', lifetime)
    print("Periods of normal use before acceptable failure (1584 hours per period): ", periods)
    print("Hours of normal use before acceptable failure: ", periods*1584)
    print("Periods of normal use during expected ownership time: ", lifetime_periods)
    print("Hours of normal use before acceptable failure: ", lifetime_periods*1584)
    print("Result ------------------------------------------------------------------------------")
    print("Probability of %d failures during acceptable time: %.2f" %(failures, prob_fail_periods))
    print("Probability of %d failures during expected ownership: %.2f" %(failures, prob_fail_lifetime))
    

def FailureRate(machine_wkhrs, dataset):
    subset = []
    for row in dataset:
        wkhrs = int(row['WorkHrs'])
        if(wkhrs <= machine_wkhrs + 500 and wkhrs >= machine_wkhrs - 500):
            subset.append(row)
    amount_failures = len(subset)
    
    return amount_failures/len(dataset)

def PoissonProb(num_events, lambda_value):
    return poisson.pmf(num_events, lambda_value)




if __name__ == "__main__":
    main()