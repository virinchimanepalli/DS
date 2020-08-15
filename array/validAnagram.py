# 242.Valid Anagram

# Given two strings s and t , write a function to determine 
# if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true


# need to optimise a little




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hm1 = dict()
        hm2 = dict()
        for i in s:
            if i in hm1.keys():
                # pass
                hm1[i]+=1
            else:
                hm1[i] = 1
                
        for i in t:
            if i in hm2.keys():
                # pass
                hm2[i]+=1
            else:
                hm2[i] = 1
        

        
        for i in s:
            if i in hm1.keys() and i in hm2.keys():
                if hm1[i] == hm2[i]:
                    pass
                else:
                    return False
            else:
                return False
        return True