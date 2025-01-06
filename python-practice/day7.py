# Question: Day 7: Write a Python function using recursion to calculate Fibonacci numbers.
def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
print(fibonacci(7))  # Should output 13
