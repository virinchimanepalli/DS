def firstUniqChar(s):
    hm = dict()
    for k in range(len(s)):
 
        if s[k] in hm.keys():
            hm[s[k]] = 10000
            # print(hm[s[k]])
        else:
            hm[s[k]] = k
        
    for i,(k,v) in enumerate(hm.items()):
        if hm[k] != 10000:
            print(hm)
            return v
        
        
    
s = "eeccododel"
print(firstUniqChar(s))