# Question: Day 58: Check palindrome ignoring case and non-alphanumeric characters.
import re

def is_palindrome(s):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama!"))  # True
