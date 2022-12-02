"""
Project 3
Auhtor @Daniel Weinert
Created on 8/3/21
"""
def Program1():
    print("""
----------------------------
    Welcome to program 1
     by Daniel Weinert
----------------------------""")
    
    #Initilize vars
    counter = 0
    userL = []
    userInput = 0
    total = 0

    #loop for input and check for existing number
    while counter != 10:
        userInput = int(input("Please enter an integer: "))
        if not userInput in userL:
            userL.append(userInput)
            counter += 1
    
    #print out list
    print(*userL, sep = ", ") 
    
    #print/calc total sum
    for x in range(len(userL)):
        total += userL[x]
    print("Total sum of the list: ", total)
    
    #print/calc total avg
    avg = total / counter
    print("Average of list is: ", avg)
    
def CountLetters(word):
    #initilize vars
    countUpper = 0
    countLower = 0
    
    #run loop for each char to check if its in the range of uppercase or lowercase letter
    for x in word:
        
        if x >= 'A' and x <= 'Z':
            countUpper += 1
        
        if x >= 'a' and x <= 'z':
            countLower += 1
    
    #return the total amount of each
    return countUpper, countLower

def Program2():
    print("""
----------------------------
    Welcome to program 2
     by Daniel Weinert
----------------------------""")
    
    #call function to count the lowercase letters and uppercase letters, pass thru input from user  
    totalUpper, totalLower = CountLetters(input("Enter a sentence to count the uppercase and lowercase letters: "))
    
    #output total count of letters
    print(f"The input contains {totalUpper} uppercase letters and {totalLower} lowercase letters")
    
def ApplyDiscount(saleA, discountP):
    discountA = saleA - (saleA * discountP)
    return discountA

def Program3():
    print("""
----------------------------
    Welcome to program 3
     by Daniel Weinert
----------------------------""")
    
    #initlize vars
    saleID = int(input("-----\nEnter first Sale ID: "))
    saleIDL = []
    saleAmountL = []
    discountPercentageL = []
    discountAmountL = []
    cnt = 0
    totalAmountDiscounts = 0.0
    avgAmountDiscounts = 0.0
    
    #loop to take in each sale
    while saleID != -1:
        saleIDL.append(int(saleID))
        saleAmountL.append(float(input("Enter sale amount: $")))
        discountPercentageL.append(float(input("Enter discount percentage (decimal): ")))
        discountAmountL.append(ApplyDiscount(saleAmountL[cnt], discountPercentageL[cnt]))
        totalAmountDiscounts += discountAmountL[cnt]
        cnt += 1
        saleID = int(input("-----\nEnter another Sale ID: "))
    
    #loop for each sale to print out data
    for x in range(len(saleIDL)):
        print(f"""--
Sale ID: {saleIDL[x]}
Sale Amount: ${round(saleAmountL[x], 2)}
Discount %: {(discountPercentageL[x])}
Discounted Sale Amount: ${round(discountAmountL[x], 2)}
--""")
        
        print(f"""
Total Amount of Discounted sales: ${round(totalAmountDiscounts, 2)}
Average Amount of Discounted sales: ${round(totalAmountDiscounts / cnt, 2)}
""")

#Launch each program
Program1()
Program2()
Program3()





