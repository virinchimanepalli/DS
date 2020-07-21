class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = dict()
        for i in range(len(nums)):
            hm[nums[i]] = i
            
        for i in range(len(nums)):
            k = target - nums[i]
            
            if k in hm.keys() and i!= hm[k]:
                return [i,hm[k]]
                


def sm(nums,target):     
    hm = dict()
    for i in range(len(nums)):
        hm[nums[i]] = i
    print(hm)       
    for i in range(len(nums)):
        k = target - nums[i]
        print(k)
        if k in hm.keys() and i != hm[k]:
            return [i,hm[k]]

nums = [3,2,4]

print(sm(nums,6))