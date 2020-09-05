# Find Pivot Index


# Given an array of integers nums, write a method that returns the "pivot" index of this array.

# We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

 

# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
# Example 2:

# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_value = 0
       
        if nums == []:
            return -1
        
        left_sum = []
        right_sum = []
        for i in range(len(nums)):
            l_value +=nums[i]
            left_sum.append(l_value)
            
        r_value= left_sum[-1]
        for i in range(len(nums)):
            right_sum.append(r_value)
            if i == len(nums)-1:
                pass
            else:
                r_value-=nums[i]
        print(left_sum,right_sum)
        
        for i in range(len(nums)):
            if i == 0:
                if right_sum[i+1] ==0:
                    return i
            elif i == len(nums)-1:
                if left_sum[i-1] == 0:
                    return i
            else:
                if left_sum[i-1] == right_sum[i+1]:
                    return i
                
        return -1