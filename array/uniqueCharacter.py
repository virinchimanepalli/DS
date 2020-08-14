# First Unique Character in a String
# Given a string, find the first non-repeating character in it and return its index.
#  If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = dict()
        for k in range(len(s)):
 
            if s[k] in hm.keys():
                hm[s[k]] = float('inf')
            else:
                hm[s[k]] = k
        
        for i,(k,v) in enumerate(hm.items()):
            if hm[k] != float('inf'):
                return v
        return -1
        