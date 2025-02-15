# Question: Day 47: Sort list of tuples by second element using lambda function.
data = [('apple', 50), ('banana', 20), ('cherry', 30)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # [('banana', 20), ('cherry', 30), ('apple', 50)]
