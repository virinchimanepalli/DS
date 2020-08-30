# 581. Shortest Unsorted Continuous Subarray
# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order

def cs(a):
    c = a.copy()
    c.sort()
    start = len(a)
    end = 0
    for i in range(len(c)):
        if c[i]!= a[i]:
            start = min(start,i)
            end = max(end,i)

    return end - start +1 if end - start >=0 else 0


a = [1,3,2,3,3]
print(cs(a))