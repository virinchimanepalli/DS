# Find All Numbers Disappeared in an Array

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) + 1
        k = [i for i in range(1,n)]

        a = set(k)
        b = set(nums)
        val = a-b
        l = [i for i in val]

        return l