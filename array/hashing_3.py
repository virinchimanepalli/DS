arr = [1, 7, 4, 3, 4, 8, 7 , 3 ,3]
l = len(arr)
k = int(input("enter k value "))

def k_times(arr,l,k):
    h =  dict()
    dummy = 0
    #  print(h.keys())
    for i in range(l):
        if arr[i] in h.keys():
            h[arr[i]] += 1
        else:
            h[arr[i]] =1
    # print(h)

    for i in range(l):
        if h[arr[i]] == k:
            dummy += 1
            print("First element occurring k times in an array is {}".format(arr[i]))
            print(h.keys())
            print(h)
            break
    if (not dummy):
        print(-1)
        

k_times(arr,l,k)


