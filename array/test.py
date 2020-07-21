# # # # arr = [[0 for i in range(2)]
# # # #            for i in range(5)]
# # # # # print(arr)
# # # # arr[0][0], arr[0][1] = 11, 20
# # # # arr[1][0], arr[1][1] = 30, 40
# # # # arr[2][0], arr[2][1] = 5, 10
# # # # arr[3][0], arr[3][1] = 40, 30
# # # # arr[4][0], arr[4][1] = 10, 5

# # # # abc = dict()

# # # # for i in range(len(arr)):
# # # #     first = arr[i][0]
# # # #     second = arr[i][1]
# # # #     if (second in abc.keys() and abc[second]== first):
# # # #         print("({},{})".format(second,first))
# # # #     else:
# # # #         abc[first] = second
# # # arr = [0, 1, 2, 6, 1]
# # # s = set()
# # # sumvalue = 6
# # # for i in  range(len(arr)):
# # #     # if arr[i] in 
# # #     temp = sumvalue - arr[i]
# # #     if temp in s:
# # #         print("({},{})".format(arr[i],temp))
    
# # #     s.add(arr[i])
# # # print(s)


# # #note: in doublehashing hashtable size should be known

# # def double_hashing(keys, hashtable_size, double_hash_value):
# #     hashtable_list = [None] * hashtable_size
# #     print(hashtable_list)
# #     for i in range(len(keys)):
# #         hashkey = keys[i] % hashtable_size
# #         print("keys[i] ={} -> hashkey ={}".format(keys[i],hashkey))
# #         if hashtable_list[hashkey] is None:
# #             # print(hashtable_list[hashkey])
# #             hashtable_list[hashkey] = keys[i]
# #             # print(hashtable_list[hashkey])
# #         else:
# #             print("else")
# #             # print(keys[i])
# #             new_hashkey = hashkey
# #             # print("newhashkey-{}".format(new_hashkey))
# #             while hashtable_list[new_hashkey] is not None:
# #                 # print(hashtable_list[new_hashkey])
# #                 steps = double_hash_value - (keys[i] % double_hash_value)
# #                 print("step-{}".format(steps))
# #                 print("newhashkey-{} steps-{}".format(new_hashkey,steps))
# #                 new_hashkey = (new_hashkey + steps) % hashtable_size  ## problem 1 is here
# #                 print(new_hashkey)
# #             hashtable_list[new_hashkey] = keys[i]

# #     return hashtable_list  ## problem 2 is here


# # values = [26, 54, 94, 17, 31, 77, 44, 51]
# # print( double_hashing(values, 13, 5) )
# # # print(hashtable_list)

# # [26, None, 54, 94, 17, 31, 44, 51, None, None, None, None, 77]
# # k = int(input())
# k = "heello"
# l= k.split()
# print(k)
# d =0
# hm = dict()
# for i in range(len(k)):
#     if k[i] in hm.keys():
#         d +=1
#         hm[k[i]] +=1
#         print(k[i])
#         break
#     else:
#         hm[k[i]] = 1
# if d == 0:
#     print(-1)
# # print(hm)

# # k = str(input("enter "))
# # print(k)
# # l= list(k)
# # print(l)
# # d =0
# # hm = dict()
# # for i in range(len(l)):
# #     if k[i] in hm.keys():
# #         d +=1
# #         hm[k[i]] +=1
# #         print(k[i])
# #         break
# #     else:
# #         hm[k[i]] = 1
# # if d == 0:
# #     print(-1)


def func(arr,size):
    if size == 1:
        return arr[0]
    m = func(arr,size-1)
    if (arr[size-1]<m):
        return arr[size-1]
    else:
        return m
    
arr = [2,3,1,4,6,34]
# print(func(arr,6))
def fizzBuzz(n):
    for i in range(1,n):
        if n%3 ==0 and n&5 !=0:
            print(n%3)
            print("Fizz")
        elif n%3 !=0 and n&5 ==0:
            print("Buzz")
        elif n%3 ==0 and n&5 ==0:
            print("FizzBuzz")
        else:
            print(n)

# fizzBuzz(15)
hm = dict()

hm[5] = 1

print(hm.keys())