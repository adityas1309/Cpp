# Question: Day 5: Write a Python program to calculate the factorial of a number using a loop.
n = int(input("Enter a number: "))
factorial = 1
# Multiply numbers from 1 to n
for i in range(1, n+1):
    factorial *= i
print(f"Factorial of {n} is {factorial}")
