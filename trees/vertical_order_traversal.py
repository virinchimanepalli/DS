# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = []
        
        #base coditions
        if root is None:
            return result
        
        self.min = 0
        self.max = 0
        cache = {}
        
        def dfs(node,r,c):
            #base condition
            if node is None:
                return 
            if c in cache:
                cache[c].append([r,node.val])
            
            else:
                cache[c] = [[r,node.val]]
            
            self.min = min(c,self.min)
            self.max = max(c,self.max)
            
            dfs(node.left,r+1,c-1)
            dfs(node.right,r+1,c+1)
            
        dfs(root,0,0)
        
        for c in range(self.min,self.max+1):
            col = sorted(cache[c], key = lambda x:(x[0],x[1]))
            col_sorted = []
            for i in col:
                col_sorted.append(i[1])
            result.append(col_sorted)
        return result
            