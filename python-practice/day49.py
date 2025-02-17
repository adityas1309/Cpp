# Question: Day 49: Generate all permutations of a list using itertools.
import itertools

def generate_permutations(lst):
    return list(itertools.permutations(lst))

print(generate_permutations([1, 2, 3]))
