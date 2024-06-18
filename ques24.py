# Python Programming Assignment-1
# 24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as 
# input and print the result. 
num1= int(input("Enter first number:"))
num2= int(input("Enter second number:"))
ope= input("Enter the operator:")
if ope=='+':
    print(num1 + num2)
elif ope=='-':
    print(num1-num2)
elif ope=='*':
    print(num1*num2)
elif ope=='/':
    print(num1/num2)
