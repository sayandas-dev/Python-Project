import math
print("Triangle Calculation Utility")
print("*************************")
print("")
p=int(input("Enter Height     :"))
b=int(input("Enter Base        :"))
print("")
area=(p*b)/2
h=round(math.sqrt(p*p)+(b*b),2)
peri=(p+b+h)
print("Area                       :",area)
print("Perpendicular        :",peri)
