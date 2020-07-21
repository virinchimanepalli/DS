def insert(a,n):
    for i in range(n):
        if a[i] >= 0:
            hashing[[a[i]][0]] =1
        else:
            hashing[abs(a[i])][1] =1

def search(f):
    if f >=0:
        return hashing[f][0] == 1
    else:
        return hashing[abs(f)][1] ==1


a = [-1, 9, -5, -8, -5, -2]
n = len(a)
maxValue = 3
hashing = [[0 for i in range(2)] for j in range(maxValue+1) ]
insert(a,n)
find = int(input("enter value:" ))
if search(find):
    print("present")
else:
    print("absent")




