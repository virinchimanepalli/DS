# 443. String Compression
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

# Every element of the array should be a character (not int) of length 1.

# After you are done modifying the input array in-place, return the new length of the array.

 
# Follow up:
# Could you solve it using only O(1) extra space?

 
# Example 1:

# Input:
# ["a","a","b","b","c","c","c"]

# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

class Solution:
    def compress(self, chars: List[str]) -> int:

        char = chars
        i = 0
        c = 1

        while i!=len(char)-1:
            if char[i] == char[i+1]:
                c+=1
                char.pop(i)
            elif char[i]!= char[i+1] and c!=1:
                for j in str(c):
                    print(j,i)
                    char.insert(i+1,str(j))
                    i+=1
                i += 1
                c = 1
            else:
                i+=1
        if c!= 1:
            k = str(c)
            for i in k:
                char.append(str(i))
        return len(char)
        


char=["a","a","a","a","a","a","a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]
i = 0
c = 1

while i!=len(char)-1:
    if char[i] == char[i+1]:
        c+=1
        char.pop(i)
    elif char[i]!= char[i+1] and c!=1:
        for j in str(c):
            print(j,i)
            char.insert(i+1,str(j))
            i+=1
        i += 1
        c = 1
    else:
        i+=1
if c!= 1:
    # if c > 9:
    k = str(c)
    for i in k:
        char.append(str(i))
print(char)
