# 383. Ransom Note
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.
# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = Counter(magazine)
        # print(hm)
        
        for i in ransomNote:
            if i in hm.keys():
                hm[i] -= 1
                if hm[i] == 0:
                    hm.pop(i)
            else:
                return False
        return True