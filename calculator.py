operator=input("Enter the operator (+,-,*,/):")
n1=float(input("enter the first number:"))
n2=float(input("enter the second number:"))

if operator == "+":
    result=n1 + n2
    print(round (result ,3))
elif operator == "-":
    result= n1 + n2
    print(round (result, 3))
elif operator == "*":
    result= n1 + n2
    print(round (result ,3))
elif operator == "/":
    result= n1 + n2
    print(round (result ,3))
else:
    print(f"{operator} is not a vaild operator")
    