def rp(A,B):
    dup = A
 
    count = 0
        
    while(True):
        if B in dup:
            return count +1
        if len(A)*count >len(B):
            return -1
        A = A+ dup
        count+=1
    

A = "abcd"
B = "cdabcdab"
print(rp(A,B))