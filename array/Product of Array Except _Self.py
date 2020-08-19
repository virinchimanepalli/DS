# 238. Product of Array Except Self

# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []
        l = len(nums) -1
        k = 1
        product = 1

        for i in range(len(nums)):
            k = k*nums[i]
            a.append(k)
        
        for i in range(len(nums)-1,0,-1):
            
            if i == len(nums)-1:
                a[i] = a[i-1]
                product = product*nums[i]
            else:
                a[i] = a[i-1]*product
                product = product*nums[i]
            
        a[0] = product
        return a
            
                
            