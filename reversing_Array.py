def reverseArray(a):
    b = []
    l = len(a)-1
    while l >=0:
        k = a.pop(l)
        b.append(k)
        l = l-1


    return b

a = [1,2,3,4]
print(reverseArray(a))