# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur_sum =nums[0]
        l = len(nums) 
        for i in range(1,l):
            cur_sum = max(nums[i],cur_sum+nums[i])
            max_sum = max(max_sum,cur_sum)
        
        return max_sum