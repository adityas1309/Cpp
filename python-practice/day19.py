# Question: Day 19: Write a Python program to flatten a nested list.
def flatten_list(nested):
    # Recursive flattening
    return [
        element 
        for sublist in nested 
        for element in (flatten_list(sublist) 
        if isinstance(sublist, list)
    ] if isinstance(nested, list) else [nested]

nested = [1, [2, [3, 4], 5]]
print("Flattened list:", flatten_list(nested))
