# Question: Day 57: Convert matrix to flattened list using list comprehension.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1,2,3,4,5,6,7,8,9]
