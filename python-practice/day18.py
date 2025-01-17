# Question: Day 18: Write a Python program to handle division with proper exception handling.
try:
    num1 = float(input("Enter dividend: "))
    num2 = float(input("Enter divisor: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input!")
else:
    print(f"Result: {result:.2f}")
