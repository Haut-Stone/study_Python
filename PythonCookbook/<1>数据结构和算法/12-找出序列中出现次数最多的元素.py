'''

'''

from collections import Counter


words = [
    'well', 'nihao', 'well', 'nihao', '123', '123', '123', '123', '123',
    'ANS', "AMS", 'ANS', 'ANS', 'OJBK', 'OJBK', 'OJBK', 'OJBK', 'MIMI'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# 计数器君在底层其实是一个字典
print(word_counts['well'])

# 你还可以对他进行一些数学上的骚操作

more_words = ['well', 'well', 'AMS', 'AMS', 'AMS']

for word in more_words:
    word_counts[word] += 1

new_top_three = word_counts.most_common(3)
print(new_top_three)

a = Counter(words)
b = Counter(more_words)
print(a)
print(b)
c = a + b
print(c)
d = a - b
print(d)
