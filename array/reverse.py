#reverse a number with out using extra space
def rp(s):
    i = 0
    j = len(s)-1
    if len(s) %2 ==0:
        # for i in range(len(s)):
        while i<j:
            s[i],s[j] = s[j],s[i]
            i +=1
            j-=1
        return s
    elif len(s) %2 !=0:
        while i!=j:
            s[i],s[j] = s[j],s[i]
            i +=1
            j-=1
        return s
s = [0,1,2,3,4,5,6,7,8]
print(rp(s))