# Python Programming Assignment-1
# 23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
def fahrenheit(n):
    fahrenheit= ((9/5)*n) +32
    return fahrenheit
def celsius(x):
    celsius= (x-32)*(5/9)
    return celsius
print(fahrenheit(32))
print(celsius(89.6))