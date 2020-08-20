# 692. Top K Frequent Words
# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]

# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4

# Output: ["the", "is", "sunny", "day"]

# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.

from heapq import heappush,heappop
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:



        counter = Counter(words)

        heap = []
        for key,count in counter.items():
            print(key,count)
            heappush(heap,(-count,key))

        print(heap)
        a = []
        for _ in range(k):
            popvalue = heappop(heap)
            a.append(popvalue[1])
        return a




from heapq import heappush,heappop
from collections import Counter

def tp(words,k):
    counter = Counter(words)

    heap = []
    # heap invarient automatically checks the albatical order
    for key,count in counter.items():
        print(key,count)
        heappush(heap,(-count,key))
    
    print(heap)
    a = []
    for _ in range(k):
        popvalue = heappop(heap)
        a.append(popvalue[1])
    return a


k = 2
words = ["i", "love", "leetcode", "i", "love", "coding"]
a = tp(words,k)
print(a[len(words)-k:len(words)])

print(tp(words,k))