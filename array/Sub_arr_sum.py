# 209. Minimum Size Subarray Sum
# import question try to to slove again 
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.



def sb(k,nums):
    i = 0
    j = 0
    c = 0
    mini = float('inf')

    while j <(len(nums)):
        c+=nums[j]#mistake1
        if c < k:
            print(j,i)
            # spot1
            j+=1
        elif c>=k:
            print(j,i)
            mini = min(mini,(j-i+1))
            print("mini - {}".format(mini))
            c = c- nums[i] -nums[j]#related to spot1
            i+=1
    return mini if mini <float('inf') else 0
    print(mini)



    # while j <=(len(nums)-1):
    #     if c < k:
    #         print(j,i)
    #         c+=nums[j]
    #         j+=1
    #     elif c>=k:
    #         print(j,i)
    #         mini = min(mini,(j-i))
    #         print("mini - {}".format(mini))
    #         c = c- nums[i]
    #         i+=1
    # return mini
    # print(mini)
s = 7
nums = [2,3,1,2,4,3]
print(sb(s,nums))