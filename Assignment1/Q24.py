'''Write a program that acts as a simple calculator. It should take two
numbers and an operator (+, -, *, /) as input and print the result.'''
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=str(input("Enter the operation:"))
if operation=='+':
    print("Sum={}".format(num1+num2))
elif operation=='-':
    if num1>num2:
        print("Difference={}".format(num1-num2))
    else:
        print("Difference={}".format(num2-num1))
elif operation=='x':
    print("Product={}".format(num1*num2))
else:
    print("Quotient={}".format(num1/num2))

