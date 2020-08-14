# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = []
        
        for i in range(len(nums)):
            index = (abs(nums[i])-1)
            if nums[index] <0:
                a.append(index+1)
            nums[index] = -nums[index]
            
        
        return a