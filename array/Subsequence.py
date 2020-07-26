# subsequence of a given string 
# returns yes  if it a contains 
# reminder of 0 or 1 or 2 in subsequence list.
def subsequence(str1):
    if len(str1) == 0:
        return [" "]
    
    small = subsequence(str1[1:len(str1)])
    
    result = [" "]*(2*len(small))
    
    k = 0
    for i in range(len(small)):
        result[k] = small[i]
        k+=1

    for i in range(len(small)):
        result[k] = str1[0]+small[i]
        k+=1
    print(result)
    return result

arr = [0,1,2]
str1 = "174"
a = subsequence(str1)
hm = dict()
hm[" "] = float("inf")
for i in a:
    if i in hm.keys():
        pass
    else:
        hm[i] =  int(i) % 9 

print(hm.values())

for i in arr:
    if i in hm.values():
        print("yes",i)
    else:
       print("no")
