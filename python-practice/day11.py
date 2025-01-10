# Question: Day 11: Write a Python program to create a list of even numbers from 1-50 using list comprehension.
# List comprehension with condition
evens = [x for x in range(1, 51) if x % 2 == 0]
print("Even numbers:", evens)
