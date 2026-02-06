a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def alu ():
        return a, b
add, sub, mul, div = a + b, a - b, a * b, a / b

print("Addition is: ", add) 
print("Subtraction is: ", sub)
print("Multiplication is: ", mul)           
print("Division is: ", float(div))  


if add % 2 == 0 and sub % 2 == 0 and mul % 2 == 0 and div % 2 == 0:
        print("All operations are Even")

elif add % 2 == 0 and sub % 2 == 0 and mul % 2 == 0 and div % 2 != 0:
        print("Addition, Subtraction and Multiplication are Even, Division is Odd")
elif add % 2 == 0 and sub % 2 == 0 and mul % 2 != 0 and div % 2 != 0:
        print("Addition and Subtraction are Even, Multiplication and Division are Odd")

elif add % 2 == 0 and sub % 2 != 0 and mul % 2 != 0 and div % 2 != 0:
        print("Addition is Even, others are Odd")

elif add % 2 != 0 and sub % 2 != 0 and mul % 2 != 0 and div % 2 != 0:
        print("All operations are Odd")

else:
        print("Mixed Even and Odd operations")