# Python Programming Assignment-1
# 11. Write a python program that generates the first n numbers in the Fibonacci sequence. 
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(2, n)]
    return fib
n = 10
fib = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {fib}")
