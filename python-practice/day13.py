# Question: Day 13: Write a Python program to find the largest number in a list without using max().
numbers = [23, 45, 12, 67, 34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"Largest number: {largest}")
