# Question: Day 28: Implement a simple Caesar cipher with variable shift value.
def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

print(caesar_cipher("Hello, World!", 3))  # Khoor, Zruog!
