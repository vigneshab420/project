# 21. Word Order - HackerRank
from collections import OrderedDict

n = int(input("Enter number of words: "))
word_count = OrderedDict()

for _ in range(n):
    word = input("Enter word: ")
    word_count[word] = word_count.get(word, 0) + 1

print(f"Distinct words: {len(word_count)}")
print("Word counts:", *word_count.values())