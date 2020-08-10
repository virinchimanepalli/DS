#left_view of a binary tree
class Node: 
  
    def __init__(self, data): 
        self.val = data 
        self.left = None
        self.right = None
        self.count = 0


def leftViewCount(root):
    if root is None: 
        return 
    
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return 1+ leftViewCount(root.right)

    else:
        return 1+ leftViewCount(root.left)


def leftTreeView(root):
    if root is None:
        return 
    # if root.left is None and root.right is None:
    #     return
    if root.left is None:
        print(root.val, end=" ")
        leftTreeView(root.right)
    else:
        print(root.val,end=" ")
        leftTreeView(root.left)

root = Node(10)  
root.left = Node(11)  
root.left.left = Node(7) 
root.left.left.left = Node(45)
# root.right = Node


leftTreeView(root)
