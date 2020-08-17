import math
def ipw(n):
    num = n
    if num <= 0:
        return False
        
    x = math.log10(num)/math.log10(4)
        

    return (math.ceil(x)==math.floor(x))


n = 2147483648
print(ipw(n))