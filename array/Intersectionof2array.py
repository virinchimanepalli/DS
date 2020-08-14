# Intersection of Two Arrays II

# Given two arrays, write a function to compute their intersection.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 == [] or nums2 == []:
            return []
        
        
        hm = dict()
        for i in nums2:
            if i in hm.keys():
                # pass
                hm[i]+=1
            else:
                hm[i] = 1
    
        
        ar = []
        for i in nums1:
            if i in hm.keys() and hm[i]!=0:
                hm[i]-=1
                ar.append(i)
            elif i in hm.keys() and hm[i] ==0:
                hm.pop(i)
        return ar