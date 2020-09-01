# 557. Reverse Words in a String III
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s
        b = ""
        k = a.split(" ")
        for i in k:

            if i == "":
                pass
            else:
                b = b + i[::-1] + " "
        return b[:-1]