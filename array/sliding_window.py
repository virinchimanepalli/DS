#Given a string, find the length of the longest substring without
#repeating characters.
#sliding window problem.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a_pointer = 0
        b_pointer = 0
        maxi = 0
        set1 = set()
        while b_pointer < len(s):
            
            if s[b_pointer] in set1:
                set1.pop()
                # a_pointer += 1
            else:
                
                set1.add(s[b_pointer])
                b_pointer +=1
                maxi = max(maxi,len(set1))
        return maxi






def rep(s):
    a_pointer = 0
    b_pointer = 0
    maxi = 0
    set1 = set()
    while b_pointer < len(s):
        #if already present in set
        if s[b_pointer] in set1:
            set1.remove(s[a_pointer])
            a_pointer += 1
        else:
            #if not present in set1
            set1.add(s[b_pointer])
            b_pointer +=1
            print(set1)
            maxi = max(maxi,len(set1))
            print(maxi)
    return maxi

s = "abcabcbb"
print(rep(s))