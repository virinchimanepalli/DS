import re

def valid():
    x ="B1CDEF2354"
    k = list(x)
    l =len(k)
    count =0
    for i in range(l):
        a = k.pop(0)

        b=str(a)
        for j in range(l):
            if b == x[j]:
                count = count+1
        if count > 1:
            print(" invalid")
            return        
        else:
            count =0

    if count ==0:
        print("valid")
            
def hackerrank()
# import re
    for _ in range(int(input())):
        s = input()
        print('Valid' if all([re.search(r, s) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', s) else 'Invalid'



def mysolution():
    x ="6LfK3X35w4"
    value = x.isalnum()
    k = list(x)
    l =len(k)
    count =0
    number =0
    upper = 0
    alpha =0
    for i in range(l):
        a = k.pop(0)
        b=str(a)

        if a.isupper():
            upper = upper +1

        if a.isdigit():
            number = number+1

        for j in range(l):
            if b == x[j] and b.isalpha():
                count = count+1

        if count > 1:
            break  
        else:
            count =0

    if count ==0 and upper >=2 and number >=3 and l ==10 and value:

        print("valid")
    else:
        print("invalid")