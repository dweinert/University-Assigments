"""
Homework 7: Program 2
Auhtor @Daniel Weinert
Created on 7/29/21
"""
print("""-----------------------
       Program 2
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
    #run for loop for each number inbetween the inputs
    for i in range(x, inputTwo):
        print(x, end=", ")
        sumX += x
        x += 1
    print("\n", sumX)
        
#check if second value is smaller
elif inputOne > inputTwo:
    #run for loop for each number inbetween the inputs
    for i in range(inputTwo, y):
        print(y, end=", ")
        sumY += y
        y -= 1
    print("\n", sumY)
    
else:
    print("Please restart program and enter two diffrent values between 0 and 100")
    