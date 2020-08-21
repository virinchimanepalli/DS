# valid palindrome #leetcode
def ip(s): 
    k = "".join(ch for ch in s if ch.isalnum())
    print(k)
    l = k[::-1]


    if k.lower() == l.lower():
        return True
    else: 
        return False
s = "A man, a plan, a canal: Panama"
print(ip(s))