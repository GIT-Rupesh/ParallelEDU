# length, breadth = map(float, input("Enter length and breadth: ").split())
# def area(l , b):
#     return l * b

# print(area(length, breadth))    

# L = int((input("Enter Length : ")))
# B = int((input("Enter Breadth : ")))
# H = int((input("Enter Height : ")))
# W = int((input("Enter Width : ")))
# R = float((input("Enter Radius : ")))     
# p = 3.14

# def area(L , B):
#     return ((L ** 2) + (B ** 2))
# print("the area of rectangle is : ", area(5 , 5))   

from numpy import rint


def area_of_circle(R):
    p = 3.14
    return p * (R ** 2) 
print("the area of circle is : ", area_of_circle(7))

def area_of_cylinder(R , H):
    p = 3.14
    return 2 * p * R * (H + R)

print("the area of cylinder is : ", area_of_cylinder(7, 10))    

def ALU( A , B):
    A = int(input("Enter first number : "))
    B = int(input("Enter second number : "))    
    return A + B , A - B , A * B , A / B
add, sub, mul, div = ALU(0, 0)
print("Addition is : ", add)    
print("Subtraction is : ", sub)
print("Multiplication is : ", mul)
print("Division is : ", float(div))    
if add > 0:
    print("Addition is Positive")
else:
    print("Addition is Negative")   

if add % 2 == 0 and sub % 2 == 0 and mul % 2 == 0 and div % 2 == 0:
    print("All operations are Even")
    if add % 2 == 0 and sub % 2 == 0 and mul % 2 == 0 and div % 2 != 0:
            print("Addition, Subtraction and Multiplication are Even Division is Odd")
            if add % 2 == 0 and sub % 2 == 0 and mul % 2 != 0 and div % 2 != 0:
                print("Addition and Subtraction are Even Multiplication and Division are Odd")
                if add % 2 == 0 and sub % 2 != 0 and mul % 2 != 0 and div % 2 != 0: 
                    print("Addition is Even, others are Odd")   
else:
    print("All operations are Odd") 