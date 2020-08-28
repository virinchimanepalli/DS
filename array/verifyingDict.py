# 953. Verifying an Alien Dictionary
# # revisite question
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        c = 0
        hm = dict()
        for i in order:
            hm[i] = c
            c+=1
        # print(hm)
        for i in range(len(words)-1):
            words1 = words[i]
            words2 = words[i+1]
            
            for k in range(min(len(words1),len(words2))):
                if words1[k]!= words2[k]:
                    if hm[words1[k]] > hm[words2[k]]:
                        return False
                    break
            else:
                if len(words1)> len(words2):
                    return False
        return True
                           
        
    