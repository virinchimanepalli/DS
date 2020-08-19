# 1502. Can Make Arithmetic Progression From Sequence

# Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
# Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

# Example 1:

# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        i = 0
        j = 1
        if len(arr) == 1:
            return True
        arr.sort()
        a = arr
        k = arr[1] - arr[0]
        
        while j!=len(a) :
            if a[j] -a[i] == k:
                i+=1
                j+=1
            else:
                return False
        return True