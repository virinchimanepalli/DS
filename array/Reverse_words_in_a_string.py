# 151.Reverse Words in a String

# Solution
# Given an input string, reverse the string word by word.

 

# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"

class Solution:
    def reverseWords(self, s: str) -> str:
        a = s
        b = ""
  
        k = a.split(" ")
        # print(k[::-1])
        for i in k[::-1]:
            if i != "":
                b = b + i + " "
        
        return b[:-1]