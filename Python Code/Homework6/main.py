"""
CIS 2110 - Homework 6: Decisions-If/Else in python
Created on 7/12/2021
@author: Daniel Weinert 
"""

"""
Homework6: Program 1: Check if a number is negative, positive or zero
@author: Daniel Weinert 
"""
def ProgramOne():
    print("\n----------------------------") #Readability
    
    #take in value from user
    checkValue = int(input("Please enter a number: "))
    
    #check to see if value is +, -, or zero
    if checkValue > 0:
        print("A: The number you entered is positive!")
    elif checkValue < 0:
        print("A: The number you entered is negative!")
    elif checkValue == 0:
        print("A: The number you entered is zero!")
        
    print("----------------------------\n") #Readability

"""
Homework6: Program 2: Find the highest number out of 3 inputs
@author: Daniel Weinert 
"""
def ProgramTwo():
    print("\n----------------------------") #Readability
    
    #take in 3 float values into a list
    numbers = [float(input("Please enter a number: ")) for x in range(3)]
    
    #check which number is the largest   
    if numbers[0] >= numbers[1] and numbers[0] >= numbers[2]:
        print("A: Your first entry is the largest number!") 
    if numbers[1] >= numbers[0] and numbers[1] >= numbers[2]:
        print("A: Your second entry is the largest number!")  
    if numbers[2] >= numbers[0] and numbers[2] >= numbers[1]:
        print("A: Your third entry is the largest number!")
        
    print("----------------------------\n") #Readability
    
"""
Homework6: Program 3: Check what a string contains
@author: Daniel Weinert 
"""
def ProgramThree():
    print("\n----------------------------") #Readability
    
    #take in the string from user
    userInput = input("Please enter a string: ")
    
    #Check if string only contains letters
    if userInput.isalpha():
        print("A: Contains only letters")
        
    #Check if string only contains uppercase letters
    if userInput.isupper():
        print("A: Contains only uppercase letters")
    
    #Check if string only contains lowercase letters
    if userInput.islower():
        print("A: Contains only lowercase letters")
    
    #Check if string only contains digits
    if userInput.isdigit():
        print("A: Contains only digits")
    
    #Check if string only contains letters or digits
    if userInput.isalpha() or userInput.isdigit():
        print("A: Contains only letters or digits")
    
    #Check if string starts with uppercase letter
    if userInput[:1].isupper():
        print("A: Starts with an uppercase letter")
        
    #Check if string ends with a period
    if userInput[-1] == ".":
        print("A: Ends with a period")
        
    print("----------------------------\n") #Readability

print("Thank you for launching homework 6 coded by @Daniel Weinert! \nProgram One (Check if a number is negative, positive or zero) is now starting:")
ProgramOne() #Run program 1
print("That was Program One. Program Two (Find the highest number out of 3 inputs) is now starting:")
ProgramTwo() #Run program 2
print("That was Program Two. Program Three (Check what a string contains) is now starting:")
ProgramThree() #Run program 3
print("That was Program Three. Thank you for completing running homework 6!")