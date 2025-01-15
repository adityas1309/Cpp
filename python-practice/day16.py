# Question: Day 16: Write a Python program to find common elements in two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# Convert to sets and find intersection
common = list(set(list1) & set(list2))
print("Common elements:", common)
