# Pascal's Triangle II
# Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

# Notice that the row index starts from 0.

def ps(k):
    a = [[1],[1,1]]

    if k == 1:
        return a[0]
    if k == 2:
        return a[-1]
    
    for x in range(3,k+1):
        v = a[-1]
        i = 0
        j = 1
        a.append([1,1])
        while j < len(v):
            # print(i,j)
            a[-1].insert(i+1,v[i]+v[j])
            # print(a[-1])
            i +=1
            j+=1
    return a[-1]

k =int(input("enter input ")) + 1
print(ps(k))