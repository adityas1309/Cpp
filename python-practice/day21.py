# Question: Day 21: Write a Python program to read a text file and count the number of lines and words.
# File handling and string methods
with open('sample.txt', 'r') as file:
    content = file.read()
    lines = content.split('\n')
    words = content.split()
print(f"Lines: {len(lines)}, Words: {len(words)}")
