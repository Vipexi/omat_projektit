#! /usr/bin/python3

user_input = int(input("Enter number:"))

i, j = 0, 1
count = 0

while count < user_input:
    print(i)
    result = i + j
    # update values
    i = j
    j = result
    count += 1

cache = {0: 0, 1: 1}

def fibonacci_of(n):
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]

[fibonacci_of(n) for n in range(15)]