"""
Homework 7: Program 3
Auhtor @Daniel Weinert
Created on 7/29/21
"""
print("""-----------------------
       Program 3
   by Daniel Weinert
        7/29/21
-----------------------
""")
#initilize vars
c = 0
userF = input("Please enter your first value: ")
userFL = []

#while loops collects inputs till user enters "done"
while userF != "done":
    userFL.append(float(userF))
    userF = input("Please enter another value or type done to finish: ")
    c += 1

#print out the meta data
print(f"""
Amount of numbers entered: {c}
Sum of all numbers: {sum(userFL)}
Average of all numbers: {sum(userFL) / c}
""")