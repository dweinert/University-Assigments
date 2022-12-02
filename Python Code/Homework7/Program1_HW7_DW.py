"""
Homework 7: Program 1
Auhtor @Daniel Weinert
Created on 7/29/21
"""
print("""-----------------------
       Program 1
   by Daniel Weinert
        7/29/21
-----------------------
""")
#Initilize vars
sumX = 0
sumY = 0

inputOne = int(input("Please enter a value between 0 and 100: "))
inputTwo = int(input("PLease enter a second value between 0 and 100: "))

x = inputOne + 1
y = inputOne - 1

print("\n")

#check if first value is smaller
if inputOne < inputTwo:
    #run while loop till it hits the bigger value
    while x != inputTwo:
        print(x, end=", ")
        sumX += x
        x += 1
    print("\n", sumX)
        
#check if second value is smaller
elif inputOne > inputTwo:
    #run while loop till it hits the bigger value
    while y != inputTwo:
        print(y, end=", ")
        sumY += y
        y -= 1
    print("\n", sumY)
    
else:
    print("Please restart program and enter two diffrent values between 0 and 100")