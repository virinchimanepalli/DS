# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        
        def get_num(n):
            total = 0
            while n >0:
                n,digit = divmod(n,10)
                total+=digit**2
            return total

        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = get_num(n)

        return n ==1