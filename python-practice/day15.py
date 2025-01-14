# Question: Day 15: Write a Python program to generate a multiplication table (1-10) for a given number.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
