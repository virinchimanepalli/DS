# Write a function that reverses a string. 
# The input string is given as an array of characters char[].

# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        if len(s) %2 ==0:
            # for i in range(len(s)):
            while i<j:
                s[i],s[j] = s[j],s[i]
                i +=1
                j-=1
            return s
        elif len(s) %2 !=0:
            while i!=j:
                s[i],s[j] = s[j],s[i]
                i +=1
                j-=1
            return s