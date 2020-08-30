# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

 

# Example 1:

# Input: [1,2,2,3]
# Output: true
# Example 2:

# Input: [6,5,4,4]
# Output: true

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        i = 0
        j = 1
        t1 = None
        t2 = True
        while j<len(A):
            if A[i]<=A[j]:
                i+=1
                j+=1
            else:
                t1 = False
                break
        if t1 ==None:
            return True
        i = 0
        j = 1
        while j < len(A):
            if A[i]>=A[j]:
                i+=1
                j+=1
            else:
                t2 = False
                break
        return (t1 or t2)
        