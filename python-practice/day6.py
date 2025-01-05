# Question: Day 6: Write a Python program to check if a string is a palindrome.
s = input("Enter a string: ").lower().replace(" ", "")
# Compare string with its reverse
print("Palindrome" if s == s[::-1] else "Not a palindrome")
