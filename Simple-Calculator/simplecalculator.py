#Get 2 operands from the user, Get the operator to be used from the user, then perform the operation
#Includes Input Validation

first=float(input("Enter Your First Number: "))
second=float(input("Enter Your Second Number: "))
operator=input("Enter Your Operator: ")


if operator=="+":
    addition=first+second
    print(f"{first}+{second}={addition}")

elif operator=="-":
    subtraction=first-second
    print(f"{first}-{second}={subtraction}")

elif operator=="*":
    multiplication=first*second 
    print(f"{first}*{second}={multiplication}")

elif operator=="/":
    if second==0:
        print("Invalid operand! Division By Zero!")
    else: 
        division=first/second
        print(f"{first}/{second}={division}")

else:
    print("Invalid Operator!")
