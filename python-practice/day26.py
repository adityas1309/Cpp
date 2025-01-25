# Question: Day 26: Merge two dictionaries and sum values for common keys.
from collections import defaultdict

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 5, 'b': 15, 'd': 25}

merged = defaultdict(int)
for d in (dict1, dict2):
    for key, value in d.items():
        merged[key] += value
print(dict(merged))  # {'a': 15, 'b': 35, 'c': 30, 'd': 25}
