# 628. Maximum Product of Three Numbers
# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:

# Input: [1,2,3]
# Output: 6

# Example 2:

# Input: [1,2,3,4]
# Output: 24
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        k = nums[0]*nums[1]*nums[2]
        ln = len(nums)-1
        l = nums[-1]*nums[ln-1]*nums[0]
        return k if l< k else l