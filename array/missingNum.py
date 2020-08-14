# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing 
# from the array.


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ln = len(nums)
        formulae = (ln*(ln+1))/2
        count = 0
        for i in range(ln):
            count = count + nums[i]
            
        return int(formulae - count)