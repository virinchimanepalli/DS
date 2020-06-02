def algo(a):
    l = len(a) -1
    for i, j in zip(range(0,l,2), range(1,l,2)):
        # print(i)
        if i+2 == l:
            mn = a[l]
            return mn
        
        if a[i] != a[j]:
            k = a[i]
            return k
    return "no single number"


a = [1, 1,2]
print(algo(a))