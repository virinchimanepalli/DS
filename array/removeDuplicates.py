# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        #slow pointer
        i = 0 
        #fast pointer
        for j in range(1,len(nums),1):
            if nums[i] != nums[j]:
        
                i+=1
                nums[i] = nums[j]
        
        return i+1
                


