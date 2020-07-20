#longest palindromic subsequence for given string (divide and conquer)

def lps(s1,st,end):
    if st > end:
        return 0
    if st == end:
        return 1


    if s1[st] == s1[end]:
        return 2 + lps(s1,st+1, end-1)
    else:
        return max(lps(s1,st+1, end), lps(s1,st, end-1))

s1 = "madam"
k = len(s1)-1
print("last index of the given string is {}".format(k))
print("longest palindromic subsequence for given string is  {}".format(lps(s1,0,k)))








