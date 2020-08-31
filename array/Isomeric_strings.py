#205.Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm = dict()
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
         
            if s[i] in hm:
                if hm[s[i]] != t[i]:
                    return False 
            else:
                if t[i] not in hm.values():
                    hm[s[i]] = t[i]
                else:
                    return False
         
        return True