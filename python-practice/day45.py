# Question: Day 45: Count word frequencies using regular expressions (ignore punctuation).
import re
from collections import defaultdict

def word_count(text):
    words = re.findall(r'\b\w+\b', text.lower())
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1
    return dict(freq)

text = "Hello! Hello world. World is awesome, hello!"
print(word_count(text))
