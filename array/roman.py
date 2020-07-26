# Integer to Roman#Leetcode amazon interview question (premium problem)
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Given an integer, convert it to a roman numeral. 
# Input is guaranteed to be within the range from 1 to 3999.


def rn(n):
    n = [int(x) for x in str(n)]
    a = []
    b = ""
    one = {1: "I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",0:""}
    second = {1:"X",2:"XX",3:"XXX",4:"XL",5:"L",6:"LX",7:"LXX",8:"LXXX",9:"XC",0:""}
    third = {1:"C",2:"CC",3:"CCC",4:"CD",5:"D",6:"DC",7:"DCC",8:"DCCC",9:"CM",0:""}
    fourth = {1:"M",2:"MM",3:"MMM",0:""}

    for i in range(len(n)):

        if len(n) == 4:
            # print(n[i])
            a.append(fourth[n[i]])
            n.pop(0) 

        if len(n) == 3:
            # print(n[i])
            a.append(third[n[i]])
            n.pop(0)      

        if len(n) == 2:
            # print(n[i])
            a.append(second[n[i]])
            n.pop(0)
        if len(n) == 1:
            a.append(one[n[i]])
            n.pop(0)
    # b = a.join()
    return b.join(a)





n = 1994


print()

print((rn(n)))