# 1486. XOR Operation in an Array
# Given an integer n and an integer start.

# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

# Return the bitwise XOR of all elements of nums.

 

# Example 1:

# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a = []
        i = 0
        
        while i <= (n)-1:
            a.append(start+2*i)
            i+=1
        k = a[0]
        for i in a[1:]:
            k=k^i
        return k
            