# Question: Day 12: Write a Python program to count the number of vowels in a string.
text = input("Enter a string: ").lower()
vowels = {'a', 'e', 'i', 'o', 'u'}
count = sum(1 for char in text if char in vowels)
print(f"Vowel count: {count}")
