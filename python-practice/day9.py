# Question: Day 9: Write a Python program to remove duplicates from a list.
original_list = [1, 2, 2, 3, 4, 4, 5]
# Convert to set and back to list
unique_list = list(set(original_list))
print("List without duplicates:", unique_list)
