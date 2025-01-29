# Question: Day 30: Implement binary search algorithm on a sorted list.
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search(sorted_list, 23))  # Index 5
