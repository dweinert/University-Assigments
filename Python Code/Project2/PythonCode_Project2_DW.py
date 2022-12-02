"""
CIS 2110 - Project 2: Python Program Listing & Sample Run
Created on 7/21/2021
@author: Daniel Weinert 
"""
#Calculate post tax amount
def GetPostTaxAmt(preAmt, taxRate):
    postAmt = preAmt * (1 + taxRate)
    return postAmt 

#Calculate totals for pre and post sale amounts
def GetTotalAmt(preAmt, postAmt, totalPreAmt, totalPostAmt):
    totalPreAmt += preAmt
    totalPostAmt += postAmt
    return totalPreAmt, totalPostAmt

#Calculate avergae amount for all sales
def GetAvgPostAmt(totalPostAmt, saleCount):
    AvgPostAmt = totalPostAmt / saleCount
    return AvgPostAmt

#Note new highest sale
def NewHighPostTaxAmt(postAmt, ID):
    highPostAmt = postAmt
    highPostAmtID = ID
    return highPostAmt, highPostAmtID

#print out start report
print("""-----------------------------------
            Project 2
   CHPC Daily Transaction Report
        by Daniel Weinert
-----------------------------------""")

#initilizae vars
saleID = ""
highPostTaxAmtID = ""
preTaxAmt = 0.0
postTaxAmt = 0.0
totalPreTaxAmt = 0.0
totalPostTaxAmt = 0.0
highPostTaxAmt = 0.0
avgPostTaxAmt = 0.0
count = 0

#input initial vars
state = input("Enter the state: ")
saleDate = input("Enter the date: ")
salesTaxRate = float(input("Enter the sales tax rate (decimal): "))

#Get first saleID
saleID = input("\nEnter the sale ID: ")

#Loop for entering sales
while (saleID != "-1"):
    count += 1
    preTaxAmt = float(input("Enter the pre-tax sale amount: "))
    postTaxAmt = GetPostTaxAmt(preTaxAmt, salesTaxRate)
    totalPreTaxAmt, totalPostTaxAmt = GetTotalAmt(preTaxAmt, postTaxAmt, totalPreTaxAmt, totalPostTaxAmt)
    avgPostTaxAmt = GetAvgPostAmt(totalPostTaxAmt, count)
    if (postTaxAmt > highPostTaxAmt):
        highPostTaxAmt, highPostTaxAmtID = NewHighPostTaxAmt(postTaxAmt, saleID)
    print(f"""
Sale Summary:
-----------------------------------
SaleID: {saleID}
Pre-Tax sale amount: {round(preTaxAmt, 2)}
Post-Tax sale amount: {round(postTaxAmt, 2)}
-----------------------------------
""")
    saleID = input("Enter the sale ID: ")

print(f"""
-----------------------------------
------CHPC: End of Day Report------
State: {state}
Date: {saleDate}
Sales Tax Rate: {salesTaxRate}
-----------------------------------
Total of all pre-tax sales: {round(totalPreTaxAmt, 2)}
Total of all post-tax sales: {round(totalPostTaxAmt, 2)}
Average of all post-tax sales: {round(avgPostTaxAmt, 2)}
Highest post-tax sale amount: {round(highPostTaxAmt, 2)}
Highest post-tax sale ID: {highPostTaxAmtID}
-----------------------------------
-----------------------------------""")
    

    
    


    


