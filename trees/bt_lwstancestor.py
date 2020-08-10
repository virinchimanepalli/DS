class Node: 
  
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
    
def lca(root,n1,n2):
    if root is None:
        return None
    
    
    if root.left is None:
        root =root.right
        lca(root,n1,n2)
        
    if root.right is None:
        root = root.left
        lca(root,n1,n2)
        
    if root.left.data != n1 and root.right.data != n2:
        if root.left.data != n2 and root.right.data != n1:
            lca(root.left,n1,n2)
            lca(root.right,n1,n2)
        # return root.data
        pass
    return root.data




root = Node(10)  
root.left = Node(11)  
root.left.right = Node(76)
root.left.left = Node(7) 
root.left.left.right = Node(45)
root.right = Node(9)  
root.right.left = Node(15)  
root.right.right = Node(8)     
# root.right.right.left(12)
# root.right.right.right = Node(81)   

lca(root,15,8)