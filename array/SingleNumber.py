# 549.Single Number
# Given a non-empty array of integers, every element appears twice except for one. Find that single one

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hm = dict()
        
        for i in nums:
            if i in hm.keys():
                hm[i] +=1
            else:
                hm[i] = 1
        
        for i in nums:
            if hm[i] == 1:
                return i
            