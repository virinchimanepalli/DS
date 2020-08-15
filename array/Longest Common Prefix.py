# Longest Common Prefix
# revisit
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        if len(strs)==0: return prefix

        for i in range(len(min(strs))):
            c=strs[0][i]
            if all(a[i]==c for a in strs):
                prefix+=c
            else:
                break
        return prefix