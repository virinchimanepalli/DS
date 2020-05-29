arr = [0, -1, 2, -3, 1]
sumvalue = int(-10)



def sum_k(arr,sumvalue):
    s = set()
    k = 0
    for i in  range(len(arr)):
        # if arr[i] in 
        temp = sumvalue - arr[i]
        if temp in s:
            print("({},{})".format(arr[i],temp))
            k +=1
        s.add(arr[i])
    # return "no valid pair"
    # print(s)
    if not k:
        print("invalid")



sum_k(arr,sumvalue)