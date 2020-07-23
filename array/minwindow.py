from collections import Counter
#minimum sliding window
#shortest length of given string
def minwindow(s,t):
    #if any one amoung is not gievn it will return ""
    if not t or not s:
        return ""

    dict_t = Counter(t)
    print(dict_t)

    #required is the uinique length of the given t(dict_t)
    required = len(dict_t)

    #left nd right pointers
    l,r = 0,0

    #It is used to trak how many unique char in window_counter.
    formed = 0


    main_count = {}

    ans = float("inf"), None,None

    while r < len(s):
        character = s[r]
        #this is very important step => any dictionary.get(keys,0)+1 
        # will create new if not present else added to the exesting one
        main_count[character] = main_count.get(character,0)+1
        
        if character in dict_t and main_count[character] ==dict_t[character]:
            formed +=1

        #if formed is equal to requried
        #in this we have to use 2 pointer tech. now we have to left pointer(skrink) towards
        # right to string the length
        while l < r and formed == required:
            character = s[l]


            #save the smaillest length value
            if r - l + 1 < ans[0]:
                mini = r - l + 1
                ans = (mini,l,r)

            main_count[character] -= 1
            if character in dict_t and main_count[character] < dict_t[character]:
                formed -= 1
            # keep moving left
            l +=1
        # keep moving right
        r+=1  
        # print(ans[0])

    if t[0] in dict_t and len(t) == 1:
        
        return t

    if ans[0] == float("inf") and s == t:
        # print(s=t)
        print(t)
        print(68468)
        return t

    print(ans)
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]



t = "a"
s = "b"
print(minwindow(s,t))
