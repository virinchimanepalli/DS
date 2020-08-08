# LEETCODE-DAY1
# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        set1 = set("abcdefghijklmnopqrstuvwxyz")
        set2 = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
        length = len(word)
        if word[0] in set2:
            if not (set(word[1:length])-set1):
                return True
            elif not (set(word[1:length])-set2):
                return True
            else:
                return False
        elif not (set(word[1:length])-set1):
            return True
        else:
            return False
            
            
            
               