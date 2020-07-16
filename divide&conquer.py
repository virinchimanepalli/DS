#1)change one string to other using divide and conquer algorithm.

def findMin(s1,s2, i1,i2):
    # print(8)
    if i1 == len(s1):
        return len(s2)- i2

    if i2 == len(s2):
        return len(s1) - i1
    
    if s1[i1] ==s2[i2]:
        return findMin(s1,s2,i1+1,i2+1)


    #delete thats why i2 is stable
    c1 = 1 + findMin(s1,s2,i1+1,i2)
    #insert thats why  i1 is stable
    c2 = 1 + findMin(s1,s2,i1,i2+1)
    #replace both will increase
    c3 = 1 + findMin(s1,s2, i1+1,i2+1)

    return min(c1,c2,c3)

s1 = "manepallivirinchi"
s2 = "manepalli"
k =findMin(s1,s2,1,1)
print("final value is {}".format(k))

