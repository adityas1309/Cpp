# Question: Day 40: Analyze text file using collections.Counter for word statistics.
from collections import Counter

def text_analyzer(filename):
    with open(filename, 'r') as f:
        content = f.read().lower()
    words = content.split()
    word_counts = Counter(words)
    print("Most common words:")
    for word, count in word_counts.most_common(5):
        print(f"{word}: {count}")

text_analyzer('sample.txt')
