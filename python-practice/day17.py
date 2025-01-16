# Question: Day 17: Write a Python program to count word frequencies in a sentence.
sentence = input("Enter a sentence: ").lower()
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word frequencies:", freq)
