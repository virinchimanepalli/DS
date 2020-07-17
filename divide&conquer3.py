# longest common subsequence.
#draw recursion for better understanding

def lcs(s1,s2,i1,i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0
    
    # c3 = 0
    if s1[i1] == s2[i2]:
        return 1 +lcs(s1,s2,i1+1,i2+1)

    else:
        return max(lcs(s1,s2,i1+1,i2),lcs(s1,s2,i1,i2+1))

    # return max(c1,c2,c3)

s1 = "abcd"
s2 = "abcd"

print(lcs(s1,s2,0,0))