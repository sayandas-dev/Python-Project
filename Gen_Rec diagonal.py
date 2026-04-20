import math
print("Diagonal Calculation Utility")
print("**************************")
print("")
a=int(input("Enter Length     : "))
b=int(input("Enter Breadth   : "))
print("")
c=round(math.sqrt((a*a)+(b*b)),2)
print("Diagonal             :",c)
