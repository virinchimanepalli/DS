# 300. Longest Increasing Subsequence
# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
def lif(arr):

    l = [1 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and l[i] <l[j] + 1:
                l[i] = l[j] +1



    return max(l)
arr = [5,8,7,1,9]
print(lif(arr))