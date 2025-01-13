# Question: Day 14: Write a Python program to check if two strings are anagrams.
def is_anagram(s1, s2):
    # Remove spaces and normalize case
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # Should return True
