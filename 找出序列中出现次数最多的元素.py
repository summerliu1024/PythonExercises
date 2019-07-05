# from collections import Counter
#
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
#     'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
#     'look', 'into', 'my', 'eyes', "you're", 'under'
# ]
#
# word_counts = Counter(words)
# top_three = word_counts.most_common(3)
# print(top_three)
#
# # 对字符串的支持
# c = Counter('abcdeabcdabcabae')  # count elements from a string
# print(c)
# print(c.most_common(3))  # three most common elements
#
# print(sorted(c))  # list all unique elements
#
# print(sorted(c.elements()))
# # for i in c.elements():
# #     print(i)
# print(''.join(sorted(c.elements())))  # list elements with repetitions
#
# print(sum(c.values()))  # total of all counts

from collections import Counter
string="""aabbccddee1234AZDEDFASFSF.,$%#@#$^*KMza1235+)("""
word_counts = Counter(string)
counts = word_counts.most_common(len(string))
print(counts)