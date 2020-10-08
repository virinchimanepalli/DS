# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1 = nums1
        nm2 = nums2
        
        numc = num1[:m]
        num1[:] = []
        # print(num1)
        # print(numc)
        p1 = 0
        p2 = 0

        while p1 < m and p2<n:
            if numc[p1] < nm2[p2]:
                num1.append(numc[p1])
                p1+=1
            else:
                num1.append(nm2[p2])
                p2+=1
        # print(num1,p2,p1)

        if p1 < m:
            for i in range(p1,m):
                num1.append(numc[i])

        if p2 < n:
            # pass
            for i in range(p2,n):
                num1.append(nm2[i])
