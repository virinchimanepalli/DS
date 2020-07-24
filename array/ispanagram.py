#hackerrank mock test question
# give an input which has set of string .we have return wheather it
#  contains all all alphabets or not.if yes it should return 1 else 0 


def isPangram(pangram):
    # Write your code here
    n = pangram
    a = []
    b = ""
    for i in range(len(n)):
        nm = n[i].replace(' ','')
        if set(nm) >= set('abcdefghijklmnopqrstuvwxyz'):
            a.append("1")
        else:
            a.append("0")
    print(a)
    return b.join(a)

k = ["abc","bca","abcdefghijklmhjknjbjnopqrstuvwxyz"]
print(isPangram(k))