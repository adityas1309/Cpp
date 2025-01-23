# Question: Day 24: Rotate a list by k elements to the right.
def rotate_list(lst, k):
    k = k % len(lst)  # Handle k > list length
    return lst[-k:] + lst[:-k]

print(rotate_list([1,2,3,4,5], 2))  # Output: [4,5,1,2,3]
