# 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

# If there is no common subsequence, return 0.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

def lcs(x,y):
    m = len(x)
    n = len(y)
    l = k = [[-1 for i in range(n+1)] for i in range(m+1)]
    print(l)
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                print(i,j,m+1,n+1)
                l[i][j] = 0
            elif x[i-1] ==y[j-1]:
                l[i][j] = l[i-1][j-1] +1 
            else:
                l[i][j] = max(l[i-1][j],l[i][j-1])
    # print(l)
    return l[m][n]
x = "AT"
y =  "ATD"


print(lcs(x,y))