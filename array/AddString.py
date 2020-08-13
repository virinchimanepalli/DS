# wrong for digits more than 10
import math
def ad(n,m):
    # pass
    n1 = []
    n2 = []
    j = ""
    hm = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    hm1 = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
    for i in n:
        n1.append(hm[i])

    for i in m:
        n2.append(hm[i])
    # print(n1)

    res =sum(d*10**i for i,d in enumerate(n1[::-1]))
    res2 =sum(d*10**i for i,d in enumerate(n2[::-1]))
    print(res+res2,"reverser")
    a = res2+res
    
    if a ==0:
        return "0"


    while True:
        if a!=0:
            if a%10 ==0:
                b = a%10
                j=j+hm1[b]
                # print(j,1)
                a=int(a/10)

                # print(j,1)

            else:
                b = a%10
                j = j + hm1[b]
                # print(j,2)
                # print(b,2)
                a = math.floor(a/10)
                print(a)
                
        else:
            break
    # print(type(j))
        # if 
    return j[::-1]
n ="17849419788197"
m="877968504004372811"
# m="0"
print(ad(n,m))