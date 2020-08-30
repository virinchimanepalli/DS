
# Pascal's Triangle
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


def ps(k):
    a = [[1],[1,1]]

    if k == 1:
        return [a[0]]
    if k == 2:
        return a
    
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
    return a

k =int(input("enter input "))
print(ps(k))
