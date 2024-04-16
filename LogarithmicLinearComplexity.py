import math

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        return math.exp(sum(math.log(i) for i in range(1, n+1)))

# Example usage:
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
