"""
find most frequent words occuring in the  txt file

"""

words =[]
with open("sample.txt") as f:
    for i in f:
        words.extend(i.split())

print(words)

from collections import Counter
count = Counter(words)
print(count.most_common(5))