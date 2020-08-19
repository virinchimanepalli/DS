#doubt
# 235.group anagram leetcode question
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
            print(ans[tuple(sorted(s))])
        return ans.values()

from collections import Counter,defaultdict,Collection
def gam(a):
    ans = collections.defaultdict(a)
    for s in a:
        ans[tuple(sorted(s))].append(s)
    return ans.values()
    
a = ["eat", "tea", "tan", "ate", "nat", "bat"]

gam(a)