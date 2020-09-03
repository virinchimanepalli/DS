# # 485.Max Consecutive Ones
# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        c = 0
        mini = float('-inf')
        while i!=len(nums):
            if nums[i] == 1:
                c+=1
                mini = max(mini,c)
                i+=1
                
            else:
                c = 0
                i+=1
        return mini if mini > float('-inf') else 0