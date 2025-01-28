# Question: Day 29: Transpose a matrix (2D list) using list comprehension.
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
print(transpose(matrix))  # [[1,4,7], [2,5,8], [3,6,9]]
