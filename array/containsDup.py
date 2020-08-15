# displays True any duplicates k available in array s

def dp(nums,k):
    hm = dict()
    for i in range(len(nums)):
        if nums[i] in hm.keys() and hm[nums[i]]!=i:
            # hm[nums[i]]= i
            print((i-hm[nums[i]]),i,nums[nums[i]])
            if (i-hm[nums[i]]) == k:
                return True
        else:
            hm[nums[i]]= i
    print(hm)
    return False

s = [1,0,1,1]
print(dp(s,1))