
class RentEquipment:
    """
        @brief - A class that calculates the cost of renting equipment
    """

    def __init__(self, rate, period, transportCost):
        """
        @param Rate - The cost per year/month/day to rent 
        @param Period - The number of years/months/days to rent
        @param TransportCost - The pickup/delivery cost
        @param rentalCost - The total rental cost  
        """
        self.rentalCost = rate * period + transportCost
        self.period = period
        self.rate = rate
        self.transportCost = transportCost

    def TotalRentalCost(self):
        """
        @return The total cost to rent
        """
        return self.rentalCost

    def RentalCostPerPeriod(self):
        """
        @return The cost to rent per period of time
        """
        return  self.rentalCost/self.period

    def RentalCostPerUsage(self, expectedHours):
        """
        @param - The amount of hours of expected use
        @return The rental cost per hour of use
        """
        return self.rentalCost/expectedHours


class BuyEquipment:
    """ A class that calculates the cost of buying equiptment """
    def __init__(self, purchaseCost, mainCost, insuranceRate, resaleValue):
        """
        @param purchaceCost - Retail cost of to purchase the equiptment
        @param mainCost - Average maintainence cost per year
        @param insuranceRate - Annual insurance cost
        @param resaleValue - Resale value of the equiptment
        """
        self.purchaseCost = purchaseCost
        self.mainCost = mainCost
        self.insuranceRate = insuranceRate
        self.resaleValue = resaleValue
        self.initialOwnershipCost = purchaseCost + mainCost + insuranceRate - resaleValue

    def OwnershipCostPerPeriod(self, period):
        """
        @param period - The number of years of ownership
        @return The ownership cost per year over a number of years
        """
        period =- 1                 # Subtract initial year
        return self.initialOwnershipCost + self.mainCost * period + self.insuranceRate * period

    def OwnershipCostPerUsage(self, expectedHours):
        """
        @param expectedHours - The amount of hours of expected work
        @return The cost per number of expected work hours
        """
        return self.initialOwnershipCost/expectedHours

    def FinancingCost(self, interest, perio):



