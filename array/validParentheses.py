# Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"{":"}","(":")","[":"]"}
    
        stack = []

        for i in s:
            if i in bracket:
                stack.append(i)

            elif stack and bracket[stack[-1]] == i:
                stack.pop()

            else:
                return False
        return stack == []