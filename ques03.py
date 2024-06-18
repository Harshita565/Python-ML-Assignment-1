# Python Programming Assignment-1
# 3. Write a python program that calculates the factorial of a given number.
def factorial (n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(2))
print(factorial(5))
print(factorial(1))