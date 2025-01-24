# Question: Day 25: Create a password validator using regular expressions (min 8 chars, mix of cases, numbers, symbols).
import re

def validate_password(password):
    return all([
        len(password) >= 8,
        re.search(r'[A-Z]', password),
        re.search(r'[a-z]', password),
        re.search(r'\d', password),
        re.search(r'[!@#$%^&*()]', password)
    ])

print(validate_password("Passw0rd!"))  # True
print(validate_password("weak"))       # False
