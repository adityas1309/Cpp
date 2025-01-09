# Question: Day 10: Write a Python program to create a simple calculator using functions.
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error"

# Calculator interface
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

operations = {
    '+': add, '-': subtract,
    '*': multiply, '/': divide
}

result = operations.get(operator, lambda: "Invalid operator")(num1, num2)
print("Result:", result)
