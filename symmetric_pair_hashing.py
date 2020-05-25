arr = [[0 for i in range(2)]
           for i in range(5)]
# print(arr)
arr[0][0], arr[0][1] = 11, 20
arr[1][0], arr[1][1] = 30, 40
arr[2][0], arr[2][1] = 5, 10
arr[3][0], arr[3][1] = 40, 30
arr[4][0], arr[4][1] = 10, 5


def find_pair(arr,row):
    hm = dict()

    for i in range(row):
        first = arr[i][0]
        second = arr[i][1]

        if (second in hm.keys() and hm[second] == first):

            print("({},{})".format(second,first))
        
        else:
            print(hm)
            hm[first] = second
            print(hm[first])
    print(hm.keys())

find_pair(arr,5)


    
        

