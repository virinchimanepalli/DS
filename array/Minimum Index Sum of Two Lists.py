# Minimum Index Sum of Two Lists
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        hm1 = dict()
        hm2 = dict()
        hm3 = dict()
        # m = ""
        mk = []
        mini = float('inf')
        for i in range(len(list1)):
            hm1[list1[i]]= i
        
        for j in range(len(list2)):
            hm2[list2[j]] = j
        
        for i in list1:
            if i in hm2.keys():
                hm3[i] = hm1[i]+hm2[i]
                if mini > (hm1[i]+hm2[i]):
                    m = i
                    mini = min(mini,hm1[i]+hm2[i])
        print(hm3)
        for i in hm3:
            if hm3[i] ==mini:
                
                mk.append(i)
        return mk
                
        
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

print(ef(list1,list2))